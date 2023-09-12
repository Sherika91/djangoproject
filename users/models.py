from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULL_BLANK


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email Address',)

    phone = models.CharField(max_length=35, verbose_name='Phone Number', **NULL_BLANK,)
    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULL_BLANK,)
    country = models.CharField(max_length=50, verbose_name='Country', **NULL_BLANK,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
