# Generated by Django 4.2.2 on 2023-09-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_telefon_st_id_telefon_st_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefon',
            name='st_id',
        ),
        migrations.AddField(
            model_name='telefon',
            name='img',
            field=models.FileField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]
