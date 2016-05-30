# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from PIL import Image

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

    def save(self, *args, **kwargs):
        super(Upload, self).save(*args, **kwargs)
        if self.image:
            image = Image.open(self.image)
            i_width, i_height = image.size
            max_size = (640,480)

            if i_width > 1000:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)
