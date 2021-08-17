import os
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class CSSImportSpec(CMSPlugin):
    REPOSITORY_CHOICES = tuple((entry.replace(settings.BASE_DIR, ''),
                                entry.replace(settings.BASE_DIR, '')) for entry in settings.STATICFILES_DIRS)
    FILE_CHOICES = []
    for i, repos in enumerate(settings.STATICFILES_DIRS):
        for r, d, f in os.walk(repos):
            for file in f:
                if not file.endswith(".css"):
                    continue
                entry = os.path.join(r, file).replace(settings.BASE_DIR, '').replace(f'{REPOSITORY_CHOICES[i][0]}/', '')
                FILE_CHOICES.append(tuple((entry, entry)))

    repository = models.CharField(
        verbose_name=_('Repository'),
        choices=REPOSITORY_CHOICES,
        blank=False,
        default='',
        max_length=1024,
        help_text=_('Select one of the statics files available folder or repository.')
    )

    css_file_path = models.CharField(
        verbose_name=_('CSS File Path'),
        choices=FILE_CHOICES,
        blank=False,
        default='',
        null=True,
        max_length=2048,
        help_text=_('File name an location inside static folder.')
    )

    def __str__(self):
        return self.css_file_path.split('/')[len(self.css_file_path.split('/')) - 1] or str(self.pk)
