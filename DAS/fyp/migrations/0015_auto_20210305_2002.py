# Generated by Django 3.0.8 on 2021-03-05 15:02

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0014_auto_20210305_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='files',
            field=models.FileField(default='settings.MEDIA_ROOT/media/avatar.png', storage=django.core.files.storage.FileSystemStorage(location='E:\\University Data\\SEMESTER 7\\Final Year Project\\Disaster-Assistant-System\\DAS\\media'), upload_to='media'),
        ),
    ]