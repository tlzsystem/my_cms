from django.db import models

class About(models.Model):
    site = models.CharField(max_length=20, primary_key=True)
    body = models.TextField()

    def __str__(self):
        return self.site