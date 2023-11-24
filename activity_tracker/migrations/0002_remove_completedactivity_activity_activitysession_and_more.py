# Generated by Django 4.2.7 on 2023-11-24 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0002_rename_exercisesteps_activitiessteps_and_more'),
        ('activity_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedactivity',
            name='activity',
        ),
        migrations.CreateModel(
            name='ActivitySession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='completedactivity',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='activity_tracker.activitysession'),
            preserve_default=False,
        ),
    ]