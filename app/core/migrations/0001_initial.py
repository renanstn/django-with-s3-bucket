# Generated by Django 4.0.4 on 2022-05-18 03:27

import app_django.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(storage=app_django.storage_backends.MediaStorage(), upload_to='')),
            ],
        ),
    ]