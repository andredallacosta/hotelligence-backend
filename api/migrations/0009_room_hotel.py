# Generated by Django 4.0.1 on 2022-03-30 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_roomtype_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='api.hotel'),
            preserve_default=False,
        ),
    ]
