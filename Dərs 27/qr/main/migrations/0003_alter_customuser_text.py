# Generated by Django 4.2.2 on 2023-10-11 19:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_customuser_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="text",
            field=models.CharField(
                max_length=50,
                validators=[django.core.validators.EmailValidator("agilli ol")],
            ),
        ),
    ]
