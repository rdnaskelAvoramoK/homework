# Generated by Django 2.2 on 2019-12-26 00:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=30)),
                ('release_date', models.DateField()),
                ('restrictions_age', models.IntegerField()),
                ('quality', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.User')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pl_title', models.CharField(max_length=30)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Hystory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewing_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapps.User')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('comment_text', models.CharField(blank=True, max_length=200, null=True)),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2019, 12, 26, 0, 38, 38, 141496, tzinfo=utc))),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.User')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.Video')),
            ],
        ),
    ]