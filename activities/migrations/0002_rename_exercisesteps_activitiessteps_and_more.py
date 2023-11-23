# Generated by Django 4.2.7 on 2023-11-23 20:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0002_rename_exercises_profile_activities'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExerciseSteps',
            new_name='ActivitiesSteps',
        ),
        migrations.RenameModel(
            old_name='Exercise',
            new_name='Activity',
        ),
        migrations.RenameField(
            model_name='activitiessteps',
            old_name='exercise',
            new_name='activity',
        ),
    ]