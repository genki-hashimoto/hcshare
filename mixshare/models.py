from django.db import models
from django.utils import timezone

class Post(models.Model):
  url = models.TextField()
  like = models.IntegerField()
  play = models.IntegerField()
  repost = models.IntegerField()
  published_date = models.DateTimeField(blank = True, null = True)
  registed_date = models.DateTimeField(default=timezone.now)
