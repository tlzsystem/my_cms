# Generated by Django 2.0.7 on 2018-08-01 03:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20180731_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 3, 30, 50, 555501, tzinfo=utc)),
        ),
    ]
