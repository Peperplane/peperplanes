# Generated by Django 4.2.5 on 2023-09-14 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("utube", "0004_playliststory_story_connect_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="videoplaylist",
            old_name="story_connect",
            new_name="first_youtuber",
        ),
        migrations.RenameField(
            model_name="videos",
            old_name="first_youuber",
            new_name="first_youtuber",
        ),
    ]
