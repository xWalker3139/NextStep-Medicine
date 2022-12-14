# Generated by Django 3.1.5 on 2022-11-25 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reteta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('imagine', models.ImageField(null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('prenume', models.CharField(max_length=264, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('nr_de_telefon', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('prenume', models.CharField(max_length=264, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('nr_de_telefon', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adauga_Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numele_cabinetului', models.CharField(max_length=264, null=True)),
                ('descriere', models.TextField(max_length=100000, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('nr_de_telefon', models.IntegerField(null=True)),
                ('localitate', models.CharField(max_length=264, null=True)),
                ('CUI', models.CharField(max_length=264, null=True)),
                ('date_firma', models.CharField(max_length=264, null=True)),
                ('registrul_comertului', models.CharField(max_length=264, null=True)),
                ('judet', models.CharField(max_length=264, null=True)),
                ('categorie', models.CharField(choices=[('Cabinet medical', 'Cabinet medical'), ('Cabinet stomatologic', 'Cabinet stomatologic')], max_length=264, null=True)),
                ('de_la1', models.CharField(choices=[('6:00', '6:00'), ('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('pana_la1', models.CharField(choices=[('6:30', '6:30'), ('7:30', '7:30'), ('8:30', '8:30'), ('9:30', '9:30'), ('10:30', '10:30'), ('11:30', '11:30'), ('12:30', '12:30'), ('13:30', '13:30'), ('14:30', '14:30'), ('15:30', '15:30'), ('16:30', '16:30'), ('17:30', '17:30'), ('18:30', '18:30'), ('19:30', '19:30'), ('20:30', '20:30'), ('21:30', '21:30'), ('22:30', '22:30'), ('23:30', '23:30'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('de_la2', models.CharField(choices=[('6:00', '6:00'), ('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('pana_la2', models.CharField(choices=[('6:30', '6:30'), ('7:30', '7:30'), ('8:30', '8:30'), ('9:30', '9:30'), ('10:30', '10:30'), ('11:30', '11:30'), ('12:30', '12:30'), ('13:30', '13:30'), ('14:30', '14:30'), ('15:30', '15:30'), ('16:30', '16:30'), ('17:30', '17:30'), ('18:30', '18:30'), ('19:30', '19:30'), ('20:30', '20:30'), ('21:30', '21:30'), ('22:30', '22:30'), ('23:30', '23:30'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('de_la3', models.CharField(choices=[('6:00', '6:00'), ('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('pana_la3', models.CharField(choices=[('6:30', '6:30'), ('7:30', '7:30'), ('8:30', '8:30'), ('9:30', '9:30'), ('10:30', '10:30'), ('11:30', '11:30'), ('12:30', '12:30'), ('13:30', '13:30'), ('14:30', '14:30'), ('15:30', '15:30'), ('16:30', '16:30'), ('17:30', '17:30'), ('18:30', '18:30'), ('19:30', '19:30'), ('20:30', '20:30'), ('21:30', '21:30'), ('22:30', '22:30'), ('23:30', '23:30'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('de_la4', models.CharField(choices=[('6:00', '6:00'), ('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('pana_la4', models.CharField(choices=[('6:30', '6:30'), ('7:30', '7:30'), ('8:30', '8:30'), ('9:30', '9:30'), ('10:30', '10:30'), ('11:30', '11:30'), ('12:30', '12:30'), ('13:30', '13:30'), ('14:30', '14:30'), ('15:30', '15:30'), ('16:30', '16:30'), ('17:30', '17:30'), ('18:30', '18:30'), ('19:30', '19:30'), ('20:30', '20:30'), ('21:30', '21:30'), ('22:30', '22:30'), ('23:30', '23:30'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('de_la5', models.CharField(choices=[('6:00', '6:00'), ('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('pana_la5', models.CharField(choices=[('6:30', '6:30'), ('7:30', '7:30'), ('8:30', '8:30'), ('9:30', '9:30'), ('10:30', '10:30'), ('11:30', '11:30'), ('12:30', '12:30'), ('13:30', '13:30'), ('14:30', '14:30'), ('15:30', '15:30'), ('16:30', '16:30'), ('17:30', '17:30'), ('18:30', '18:30'), ('19:30', '19:30'), ('20:30', '20:30'), ('21:30', '21:30'), ('22:30', '22:30'), ('23:30', '23:30'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('de_la6', models.CharField(choices=[('6:00', '6:00'), ('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('pana_la6', models.CharField(choices=[('6:30', '6:30'), ('7:30', '7:30'), ('8:30', '8:30'), ('9:30', '9:30'), ('10:30', '10:30'), ('11:30', '11:30'), ('12:30', '12:30'), ('13:30', '13:30'), ('14:30', '14:30'), ('15:30', '15:30'), ('16:30', '16:30'), ('17:30', '17:30'), ('18:30', '18:30'), ('19:30', '19:30'), ('20:30', '20:30'), ('21:30', '21:30'), ('22:30', '22:30'), ('23:30', '23:30'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('de_la7', models.CharField(choices=[('6:00', '6:00'), ('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('pana_la7', models.CharField(choices=[('6:30', '6:30'), ('7:30', '7:30'), ('8:30', '8:30'), ('9:30', '9:30'), ('10:30', '10:30'), ('11:30', '11:30'), ('12:30', '12:30'), ('13:30', '13:30'), ('14:30', '14:30'), ('15:30', '15:30'), ('16:30', '16:30'), ('17:30', '17:30'), ('18:30', '18:30'), ('19:30', '19:30'), ('20:30', '20:30'), ('21:30', '21:30'), ('22:30', '22:30'), ('23:30', '23:30'), ('24:00', '24:00'), ('Inchis', 'Inchis')], max_length=264, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
