# Generated by Django 4.2.7 on 2023-12-08 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_date_monifide_profile_date_monified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='date_monified',
            new_name='date_modified',
        ),
    ]
