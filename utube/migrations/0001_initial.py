# Generated by Django 4.2.5 on 2023-09-13 12:36

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=30)),
                ("message", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="contact_imges"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Playliststory",
            fields=[
                ("playlist_name", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="playlist_story"
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=None,
                        populate_from="playlist_name",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StoryConnect",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=30)),
                ("title", models.CharField(max_length=100)),
                ("subtitle", models.CharField(blank=True, max_length=50, null=True)),
                ("story", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="storyconnect_imges"
                    ),
                ),
                ("url", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=None,
                        populate_from="title",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Videos",
            fields=[
                ("title", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="video_imgs")),
                ("desc", models.TextField()),
                ("url", models.CharField(max_length=150)),
                ("time_stamp", models.DateField(auto_now_add=True)),
                ("genres", models.CharField(blank=True, max_length=30, null=True)),
                ("language", models.CharField(default="Telugu", max_length=50)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=None,
                        populate_from="title",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Story",
            fields=[
                ("title", models.CharField(max_length=100)),
                ("subtitle", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="story_imges"),
                ),
                ("story_info", models.TextField()),
                ("time_stamp", models.DateField(auto_now_add=True)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=None,
                        populate_from="title",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "plalist",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="utube.playliststory",
                    ),
                ),
            ],
        ),
    ]
