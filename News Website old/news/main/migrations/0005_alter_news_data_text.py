# Generated by Django 4.2.2 on 2023-11-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_news_data_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news_data",
            name="text",
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
