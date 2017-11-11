from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


