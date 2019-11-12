# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import filer.fields.file
from cmsplugin_filer_video import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerVideo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('movie_url', models.CharField(help_text='vimeo or youtube video url. Example: http://www.youtube.com/watch?v=YFa59lK-kpo', max_length=255, null=True, verbose_name='movie url', blank=True)),
                ('width', models.PositiveSmallIntegerField(verbose_name='width', default=settings.VIDEO_WIDTH)),
                ('width_units', models.CharField(verbose_name="width units", max_length=2, default=settings.VIDEO_UNITS)),
                ('height', models.PositiveSmallIntegerField(verbose_name='height', default=settings.VIDEO_HEIGHT)),
                ('height_units', models.CharField(verbose_name="height units", max_length=2, default=settings.VIDEO_UNITS)),
                ('auto_play', models.BooleanField(verbose_name='auto play', default=settings.VIDEO_AUTOPLAY)),
                ('controls', models.BooleanField(verbose_name='controls', default=settings.VIDEO_CONTROLS)),
                ('muted', models.BooleanField(verbose_name='muted', default=settings.VIDEO_MUTED)),
                ('loop', models.BooleanField(verbose_name='loop', default=settings.VIDEO_LOOP)),
                ('preload', models.CharField(verbose_name='preload', default=settings.VIDEO_PRELOAD, max_length=16)),
                ('image', filer.fields.image.FilerImageField(null=True, to='filer.Image', help_text='preview image file', related_name='filer_video_image', blank=True, verbose_name='image', on_delete=models.SET_NULL)),
                ('movie', filer.fields.file.FilerFileField(null=True, to='filer.File', help_text='use .flv file or h264 encoded video file', blank=True, verbose_name='movie file', on_delete=models.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
