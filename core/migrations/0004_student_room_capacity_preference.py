# Generated by Django 4.2.1 on 2023-05-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='room_capacity_preference',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]