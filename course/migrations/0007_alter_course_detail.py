# Generated by Django 4.1.2 on 2022-12-10 13:31

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_images_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
