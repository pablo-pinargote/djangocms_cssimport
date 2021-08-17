from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CSSImportSpec(CMSPlugin):
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    css_file_path = models.CharField(
        verbose_name=_('Alternative Text'),
        blank=True,
        null=True,
        max_length=2048,
        help_text=_('File name an location inside static folder.')
    )

    def __str__(self):
        return self.label or str(self.pk)
