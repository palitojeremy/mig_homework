from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
