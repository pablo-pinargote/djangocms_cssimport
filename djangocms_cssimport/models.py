import os
from google.cloud import storage
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.functional import lazy


class CSSImportSpec(CMSPlugin):

    REPOSITORY_CHOICES = tuple((entry.replace(settings.BASE_DIR, ''),
                                entry.replace(settings.BASE_DIR, '')) for entry in settings.STATICFILES_DIRS)

    repository = models.CharField(
        verbose_name=_('Repository'),
        choices=REPOSITORY_CHOICES,
        blank=False,
        default='',
        max_length=1024,
        help_text=_('Select a static files repository.')
    )

    css_file_path = models.CharField(
        verbose_name=_('CSS File Path'),
        choices=(),
        blank=False,
        default='',
        null=True,
        max_length=2048,
        help_text=_('Select a CSS file.')
    )

    def __str__(self):
        self._meta.get_field('css_file_path').choices = lazy(self.get_file_choices, list)()
        return self.css_file_path.split('/')[len(self.css_file_path.split('/')) - 1] or str(self.pk)

    def get_file_choices(self):

        if getattr(settings, 'GS_STATIC_BUCKET_NAME', None) is not None:
            return self.get_file_choices_from_google_storage()

        return self.get_file_choices_from_local_folder()

    def get_file_choices_from_local_folder(self):
        file_choices = []

        for i, repo in enumerate(settings.STATICFILES_DIRS):
            for r, d, f in os.walk(repo):
                for file in f:
                    if not file.endswith(".css"):
                        continue
                    entry = os.path.join(r, file)
                    entry = entry.replace(settings.BASE_DIR, '')
                    entry = entry.replace(f'{self.REPOSITORY_CHOICES[i][0]}/', '')
                    file_choices.append(tuple((entry, entry)))
        return file_choices

    def get_file_choices_from_google_storage(self):
        file_choices = []

        for i, repo in enumerate(settings.STATICFILES_DIRS):
            for prefix in os.listdir(repo):
                storage_client = storage.Client()
                blobs = storage_client.list_blobs(settings.GS_STATIC_BUCKET_NAME, prefix=prefix)
                for blob in blobs:
                    if blob.content_type != 'text/css':
                        continue
                    file_choices.append(tuple((blob.name, blob.name)))
        return file_choices
