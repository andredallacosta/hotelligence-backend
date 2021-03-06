# Generated by Django 4.0.1 on 2022-04-01 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('avaliable', 'Disponível'), ('booked', 'Reservado'), ('occupied', 'Ocupado'), ('in_cleaning', 'Em Limpeza'), ('in_maintenance', 'Em Manutenção')], default='avaliable', max_length=40),
        ),
    ]
