from django.db import models
from django.contrib.auth.models import User, PermissionsMixin,Group


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    members = models.ManyToManyField(User, related_name='memebers', blank=True)

    def __str__(self):
        return self.title
