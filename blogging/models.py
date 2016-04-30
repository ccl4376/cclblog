# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    date_time = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.name



def get_image_path(instance, filename):
    return '/'.join(['blog_images', instance.bupimg.slug, filename])

class Upload(models.Model):
    bupimg = models.ForeignKey(blog, related_name="uploads")
    image = models.ImageField(upload_to=get_image_path)
