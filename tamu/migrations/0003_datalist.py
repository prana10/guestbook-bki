# Generated by Django 4.0.2 on 2022-03-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamu', '0002_alter_tamu_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('divisi', models.TextField()),
            ],
        ),
    ]
