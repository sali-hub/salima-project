# Generated by Django 2.2.10 on 2020-12-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20201228_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multistepformmodel',
            name='document',
            field=models.FileField(upload_to='uploadfiles/'),
        ),
    ]
