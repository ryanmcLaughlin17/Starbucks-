# Generated by Django 4.1.7 on 2023-03-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_size_favourite_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]