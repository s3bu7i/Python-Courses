# Generated by Django 4.2.2 on 2023-11-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_alter_news_data_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="news_data",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]