from django.db import models
from django.contrib.auth.hashers import make_password

class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    school = models.CharField(max_length=255, default="NYU")
    grade = models.CharField(max_length=20, default="Freshman")

    def __str__(self):
        return self.name