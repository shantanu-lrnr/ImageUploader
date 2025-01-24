from django.contrib import admin
from .models import Image

# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Image._meta.get_fields()]
