from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FilerImageConfig(AppConfig):
    name = 'cmsplugin_filer_image'
    verbose_name = _('django filer image')
