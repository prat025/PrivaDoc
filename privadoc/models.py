from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    holder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
