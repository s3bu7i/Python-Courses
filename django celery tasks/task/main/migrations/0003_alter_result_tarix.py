# Generated by Django 4.2.2 on 2023-12-15 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_remove_result_text_result_num"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="tarix",
            field=models.DateTimeField(
                db_index=True, default=django.utils.timezone.now
            ),
        ),
    ]
