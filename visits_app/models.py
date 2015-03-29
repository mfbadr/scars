from django.db import models

# Create your models here.

class Visit(models.Model):

  time = models.DateTimeField(auto_now_add=True)

  summary = models.CharField(max_length=256)

  browser = models.CharField(max_length=128)
  browser_version = models.CharField(max_length=128)

  os = models.CharField(max_length=128)
  os_version = models.CharField(max_length=128)

  device = models.CharField(max_length=128)

  is_mobile = models.BooleanField()
  is_tablet = models.BooleanField()
  is_pc = models.BooleanField()

  is_bot = models.BooleanField()

  def __str__(self):
    return self.summary


