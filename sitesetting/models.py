from django.db import models

class SiteSetting(models.Model):
    site= models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    twitter = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return self.site
