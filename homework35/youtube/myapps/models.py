from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    age = models.IntegerField()
    photo = models.ImageField()


class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=30)
    release_date = models.DateField()
    restrictions_age = models.IntegerField()
    quality = models.IntegerField()


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    author_name = models.CharField( max_length=50)
    comment_text = models.CharField(null=True, blank=True, max_length=200)
    comment_date = models.DateTimeField(default=timezone.now())


class Channel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField()


class Playlist(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    pl_title = models.CharField(max_length=30)


class Hystory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    viewing_time = models.DateTimeField(auto_now_add=True)

