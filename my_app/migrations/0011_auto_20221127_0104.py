# Generated by Django 3.1.5 on 2022-11-26 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_auto_20221126_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adauga_cabinet',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='adauga_cabinet',
            name='specializare',
        ),
    ]
