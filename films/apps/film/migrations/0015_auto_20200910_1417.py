# Generated by Django 3.0.6 on 2020-09-10 10:17

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0014_auto_20200910_1410'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AddField(
            model_name='film',
            name='path_video',
            field=models.FileField(blank=True, null=True, upload_to='video', verbose_name='path video'),
        ),
        migrations.AlterField(
            model_name='film',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='embed video'),
        ),
    ]
