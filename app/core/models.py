from django.db import models
from app_django.storage_backends import MediaStorage


class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=MediaStorage())
