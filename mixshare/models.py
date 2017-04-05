from django.db import models
from django.utils import timezone

class Post(models.Model):
  url = models.TextField()
  like = models.IntegerField()
  play = models.IntegerField()
  repost = models.IntegerField()
  registed_date = models.DateTimeField(default=timezone.now)
