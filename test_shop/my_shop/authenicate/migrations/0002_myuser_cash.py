# Generated by Django 2.2 on 2020-01-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenicate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='cash',
            field=models.FloatField(default=10000),
        ),
    ]
