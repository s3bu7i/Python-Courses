# Generated by Django 4.2.2 on 2023-12-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_remove_news_data_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="news_data",
            name="view",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
