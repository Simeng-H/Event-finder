# Generated by Django 3.1.1 on 2020-10-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinder', '0002_event_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
