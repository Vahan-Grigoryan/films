# Generated by Django 3.0.6 on 2020-08-29 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_auto_20200829_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LikedFilmes',
            new_name='LikedFilms',
        ),
    ]