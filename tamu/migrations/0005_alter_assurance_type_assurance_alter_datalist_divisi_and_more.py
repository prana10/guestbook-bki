# Generated by Django 4.0.2 on 2022-03-14 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamu', '0004_assurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assurance',
            name='type_assurance',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='divisi',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='appointment_with',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='necessary',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='origin_of_company',
            field=models.CharField(max_length=500),
        ),
    ]
