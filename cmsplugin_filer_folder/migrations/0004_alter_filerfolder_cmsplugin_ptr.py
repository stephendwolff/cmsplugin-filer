# Generated by Django 4.2 on 2023-05-30 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('cmsplugin_filer_folder', '0003_auto_20160713_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerfolder',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin'),
        ),
    ]
