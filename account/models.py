from django.db import models
from django.contrib.auth.models import AbstractUser

class myUser(AbstractUser):
    age = models.CharField(max_length = 15)
    grade = models.CharField(max_length = 15)
# Create your models here.
