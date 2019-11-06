# -*- coding: utf-8 -*-
from cmsplugin_filer_file import __version__  # NOQA

from django.db import models


class FilerPluginManager(models.Manager):
    def __init__(self, select_related=None):
        self._select_related = select_related
        super(FilerPluginManager, self).__init__()
