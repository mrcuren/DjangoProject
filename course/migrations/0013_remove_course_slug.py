# Generated by Django 4.1.2 on 2022-12-17 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
    ]