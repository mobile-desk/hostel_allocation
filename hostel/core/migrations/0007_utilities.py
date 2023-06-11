# Generated by Django 4.2.1 on 2023-06-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_room_students_in_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan', models.BooleanField(default=True)),
                ('bed', models.BooleanField(default=True)),
                ('mattress', models.BooleanField(default=True)),
                ('pillows', models.BooleanField(default=True)),
                ('wardrobe', models.BooleanField(default=True)),
                ('book_rack', models.BooleanField(default=True)),
                ('tables', models.BooleanField(default=True)),
                ('chairs', models.BooleanField(default=True)),
                ('wall_socket', models.BooleanField(default=True)),
                ('tiles', models.BooleanField(default=True)),
                ('paint', models.BooleanField(default=True)),
                ('window', models.BooleanField(default=True)),
                ('waste_bin', models.BooleanField(default=True)),
                ('door', models.BooleanField(default=True)),
                ('door_lock', models.BooleanField(default=True)),
                ('bulb', models.BooleanField(default=True)),
                ('wiring', models.BooleanField(default=True)),
                ('shower', models.BooleanField(default=True)),
                ('towel_holder', models.BooleanField(default=True)),
                ('tap', models.BooleanField(default=True)),
                ('water_closet', models.BooleanField(default=True)),
                ('TV', models.BooleanField(default=True)),
                ('decoder', models.BooleanField(default=True)),
                ('other', models.BooleanField(default=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hostel')),
            ],
        ),
    ]