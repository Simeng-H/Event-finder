# Generated by Django 3.1.1 on 2020-11-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinder', '0005_merge_20201020_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
