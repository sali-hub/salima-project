# Generated by Django 2.2.10 on 2020-12-30 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]