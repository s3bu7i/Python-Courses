# Generated by Django 4.2.2 on 2023-09-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_student_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('dioqonal', models.CharField(blank=True, max_length=100, null=True)),
                ('prosessor', models.CharField(blank=True, max_length=100, null=True)),
                ('nuve_sayi', models.CharField(blank=True, max_length=100, null=True)),
                ('ram', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
