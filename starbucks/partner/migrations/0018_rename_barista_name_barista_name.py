# Generated by Django 4.1.7 on 2023-03-22 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0017_rename_name_barista_barista_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barista',
            old_name='barista_name',
            new_name='name',
        ),
    ]