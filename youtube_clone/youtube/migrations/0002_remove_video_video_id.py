# Generated by Django 3.2.7 on 2021-09-16 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_id',
        ),
    ]