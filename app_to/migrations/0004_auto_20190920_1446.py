# Generated by Django 2.0.5 on 2019-09-20 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_to', '0003_auto_20190918_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obj',
            name='file_contract',
        ),
        migrations.RemoveField(
            model_name='obj',
            name='file_defect',
        ),
        migrations.RemoveField(
            model_name='obj',
            name='file_schedule',
        ),
        migrations.RemoveField(
            model_name='obj',
            name='status_to',
        ),
    ]
