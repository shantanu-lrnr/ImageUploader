from django.db import models

# Create your models here.

class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
