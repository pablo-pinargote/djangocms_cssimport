from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from djangocms_cssimport.models import CSSImportSpec


@plugin_pool.register_plugin
class CSSImportPlugin(CMSPluginBase):
    model = CSSImportSpec
    name = _('CSS Import')
    cache = False

    @staticmethod
    def get_render_template(context, instance, placeholder):
        return 'djangocms_cssimport/default/cssimport.html'

    def render(self, context, instance, placeholder):
        return super().render(context, instance, placeholder)
