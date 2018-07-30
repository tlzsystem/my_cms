from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES =(
        ('PUBLISHED','PUBLISHED'),
        ('DRAFT','DRAFT'),
    )

    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='DRAFT')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save()
    class Meta:
        ordering = ['-created',]



