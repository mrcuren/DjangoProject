# Generated by Django 4.1.2 on 2022-12-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_contactformmessage_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformmessage',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
