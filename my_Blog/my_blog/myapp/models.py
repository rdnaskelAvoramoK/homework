from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
from django.urls import reverse


GENRE_CHOICES = (
    (1, _("Not selected")),
    (2, _("Comedy")),
    (3, _("Action")),
    (4, _("Beauty")),
    (5, _("Science")),
    (6, _("Philosophy")),
    (7, _("Other"))
)


class Author(models.Model):
    pseudonym = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=100, null=True)
    text = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=1)

    def __str__(self):
        return "id - {}, Author -{}, Title - {}, Genre - {}".format(self.id, self.author.name, self.title, self.genre)

    def get_absolute_url(self):
        return reverse('detail_article', kwargs={'pk': self.id})



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)