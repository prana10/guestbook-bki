# Generated by Django 4.0.2 on 2022-03-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamu', '0005_alter_assurance_type_assurance_alter_datalist_divisi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamu',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
