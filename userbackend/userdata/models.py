from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.urls import reverse

# Create your models here.
class UploadedImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name