# Generated by Django 5.0.1 on 2024-01-31 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedoedPJ', '0004_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
