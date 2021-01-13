# Generated by Django 2.2.10 on 2020-12-29 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20201229_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiStepFormModelBr',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Tname', models.CharField(max_length=225)),
                ('fname', models.CharField(max_length=225)),
                ('You_are', models.CharField(max_length=225)),
                ('age', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('wilaya', models.CharField(max_length=225)),
                ('fullAddress', models.CharField(max_length=225)),
                ('Email', models.CharField(max_length=225)),
                ('mainPhoneNumber', models.CharField(max_length=225)),
                ('hadena_name', models.CharField(max_length=225)),
                ('legal_status', models.CharField(max_length=225)),
                ('numemployees', models.CharField(blank=True, max_length=225, null=True)),
                ('creation_date', models.CharField(max_length=225)),
                ('nif', models.CharField(max_length=225)),
                ('nis', models.CharField(max_length=225)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/incubator')),
                ('file_CV', models.FileField(blank=True, null=True, upload_to='uploads/incubator')),
                ('file_Br', models.FileField(blank=True, null=True, upload_to='uploads/incubator')),
                ('file_CNAS', models.FileField(blank=True, null=True, upload_to='uploads/incubator')),
                ('prjdesc', models.CharField(max_length=225)),
                ('file_dev', models.FileField(blank=True, null=True, upload_to='uploads/incubator')),
                ('listequip', models.CharField(max_length=225)),
                ('file_pres', models.FileField(blank=True, null=True, upload_to='uploads/incubator')),
                ('listincubated', models.CharField(max_length=225)),
                ('file_cv_founder', models.FileField(blank=True, null=True, upload_to='uploads/incubator')),
            ],
        ),
        migrations.AlterField(
            model_name='multistepformmodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='multistepformmodel',
            name='file_Br',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='multistepformmodel',
            name='file_CV',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]