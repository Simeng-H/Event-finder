# Generated by Django 3.1.1 on 2020-11-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20201117_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='/user_avatars/default.jpg', upload_to='user_avatars'),
        ),
    ]
