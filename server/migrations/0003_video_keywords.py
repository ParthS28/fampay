# Generated by Django 3.2.4 on 2021-06-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_alter_video_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='keywords',
            field=models.CharField(default='', max_length=100),
        ),
    ]