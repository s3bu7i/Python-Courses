# Generated by Django 4.2.2 on 2023-12-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="text",
        ),
        migrations.AddField(
            model_name="result",
            name="num",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
