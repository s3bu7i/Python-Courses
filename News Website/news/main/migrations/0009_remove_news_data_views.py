# Generated by Django 4.2.2 on 2023-12-01 11:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_news_data_views"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news_data",
            name="views",
        ),
    ]
