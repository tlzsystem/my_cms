from django.db import models

class SiteSetting(models.Model):
    site= models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)

