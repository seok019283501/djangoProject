# Generated by Django 4.1 on 2022-12-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="title",
            field=models.CharField(default="", max_length=200),
        ),
    ]
