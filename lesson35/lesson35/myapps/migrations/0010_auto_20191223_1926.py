# Generated by Django 2.2 on 2019-12-23 19:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0009_auto_20191223_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='like',
            name='counter',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 23, 19, 26, 53, 851215, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 23, 19, 26, 53, 851625, tzinfo=utc)),
        ),
    ]
