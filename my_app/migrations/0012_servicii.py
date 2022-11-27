# Generated by Django 3.1.5 on 2022-11-26 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0011_auto_20221127_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicii',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('Cabinet medical', 'Cabinet medical'), ('Cabinet stomatologic', 'Cabinet stomatologic')], max_length=264, null=True)),
                ('servicii', models.CharField(choices=[('Chirurgie', 'Chirurgie'), ('Cardiologie', 'Cardiologie'), ('Pediatrie', 'Pediatrie'), ('Neurologie', 'Neurologie'), ('Oftalmologie', 'Oftalmologie'), ('Pshihiatrie', 'Pshihiatrie'), ('Radiologie', 'Radiologie'), ('PROFILAXIE', 'PROFILAXIE'), ('ODONTOTERAPIE', 'ODONTOTERAPIE'), ('ESTETICĂ', 'ESTETICĂ'), ('PEDODONȚIE', 'PEDODONȚIE'), ('ENDODONȚIE', 'ENDODONȚIE'), ('PARODONTOLOGIE', 'PARODONTOLOGIE'), ('ORTODONȚIE', 'ORTODONȚIE'), ('CHIRURGIE ȘI IMPLANTOLOGIE', 'CHIRURGIE ȘI IMPLANTOLOGIE'), ('PROTETICĂ FIXĂ ȘI MOBILĂ', 'PROTETICĂ FIXĂ ȘI MOBILĂ')], max_length=264, null=True)),
                ('pret', models.IntegerField(null=True)),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.adauga_cabinet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
