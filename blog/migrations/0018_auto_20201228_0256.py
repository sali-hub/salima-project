# Generated by Django 2.2.10 on 2020-12-28 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20201228_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multistepformmodel',
            name='prjfield',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='multistepformmodel',
            name='prjprgress',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='multistepformmodel',
            name='wilaya',
            field=models.CharField(max_length=225),
        ),
    ]
