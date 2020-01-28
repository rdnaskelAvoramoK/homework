from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class MyUser(AbstractUser):

    cash = models.FloatField(default=10000)



