# Generated by Django 4.2.7 on 2023-11-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_tracker', '0004_activitysession_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedactivity',
            name='date_completed',
        ),
        migrations.AddField(
            model_name='activitysession',
            name='date_completed',
            field=models.DateField(default='2023-11-24'),
            preserve_default=False,
        ),
    ]
