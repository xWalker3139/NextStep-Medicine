# Generated by Django 3.1.5 on 2022-11-27 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0013_servicii_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recenzii',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriere', models.TextField(max_length=10000, null=True)),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.adauga_cabinet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
