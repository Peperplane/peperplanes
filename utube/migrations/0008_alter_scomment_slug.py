# Generated by Django 4.2.5 on 2023-09-14 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("utube", "0007_vcomment_scomment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scomment",
            name="slug",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="utube.playliststory"
            ),
        ),
    ]
