from django.db import models

# Create your models here.

class Visit(models.Model):

  time = models.DateTimeField(auto_now_add=True)

  browser = models.CharField(max_length=128)
  os = models.CharField(max_length=128)
  device = models.CharField(max_length=128)

  is_mobile = models.BooleanField()
  is_tablet = models.BooleanField()
  is_pc = models.BooleanField()

  is_bot = models.BooleanField()


