# Generated by Django 4.0.1 on 2022-03-30 03:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('double_bed_quantity', models.IntegerField(blank=True, null=True)),
                ('single_bed_quantity', models.IntegerField(blank=True, null=True)),
                ('bathroom_quantity', models.IntegerField(blank=True, null=True)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('fridge', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='api.roomtype'),
        ),
    ]