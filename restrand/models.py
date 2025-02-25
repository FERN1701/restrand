from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
import random
import string


class User(AbstractUser):
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=200, null=True)
    Contact = models.IntegerField(null=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(upload_to="Profiles", null=True, default="Profiles/avatar.png")
    code = models.IntegerField(blank=True, null=True)  # Allow blank and null values
    status = models.CharField(default="notverified", max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class setting_detail(models.Model):
    details = models.TextField()

class team_detail(models.Model):
    team_image = models.ImageField(upload_to="team", height_field=None, width_field=None, max_length=None)
    team_name = models.CharField(max_length=100)
    team_description = models.TextField()
    

