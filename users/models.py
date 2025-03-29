from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Users(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Почта", help_text="укажите почту")