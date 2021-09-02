import os
from google.cloud import storage
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.functional import lazy


class CSSImportSpec(CMSPlugin):

    css_file_path = models.CharField(
        verbose_name=_('CSS File Path'),
        choices=(),
        null=True,
        blank=True,
        max_length=2048,
        help_text=_('Select a CSS file.')
    )

    def __init__(self, *args, **kwargs):
        super(CSSImportSpec, self).__init__(*args, **kwargs)
        self._meta.get_field('css_file_path').choices = lazy(self.get_file_choices, list)()

    def __str__(self):
        return self.css_file_path.split('/')[len(self.css_file_path.split('/')) - 1] or str(self.pk)

    def get_file_choices(self):
        if getattr(settings, 'GS_STATIC_BUCKET_NAME', None) is not None:
            return self.get_file_choices_from_google_storage()
        return self.get_file_choices_from_local_folder()

    def get_file_choices_from_local_folder(self):
        file_choices = []
        for i, repo in enumerate(settings.STATICFILES_DIRS):
            choices = []
            for r, d, f in os.walk(repo):
                for file in f:
                    if not file.endswith(".css"):
                        continue
                    entry = os.path.join(r, file)
                    entry = entry.replace(settings.BASE_DIR, '')
                    parent_dir = repo.replace(settings.BASE_DIR, '')
                    entry = entry.replace(f'{parent_dir}/', '')
                    choices.append(tuple((entry, entry)))
            file_choices.append((repo.replace(settings.BASE_DIR, ''), choices))
        return file_choices

    def get_file_choices_from_google_storage(self):
        file_choices = []
        for i, repo in enumerate(settings.STATICFILES_DIRS):
            choices = []
            for prefix in os.listdir(repo):
                storage_client = storage.Client()
                blobs = storage_client.list_blobs(settings.GS_STATIC_BUCKET_NAME, prefix=prefix)
                for blob in blobs:
                    if blob.content_type != 'text/css':
                        continue
                    choices.append(tuple((blob.name, blob.name)))
            file_choices.append((repo.replace(settings.BASE_DIR, ''), choices))
        return file_choices
