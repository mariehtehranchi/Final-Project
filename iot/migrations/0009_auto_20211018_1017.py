# Generated by Django 3.2.8 on 2021-10-18 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0008_auto_20211018_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='setpoint_h',
            new_name='control_h',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='setpoint_t',
            new_name='control_t',
        ),
    ]
