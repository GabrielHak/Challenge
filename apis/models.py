from django.db import models

# Create your models here.
class Apis(models.Model):
    api = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    auth = models.CharField(max_length=250)
    https = models.CharField(max_length=250)
    cors = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    category = models.CharField(max_length=250)