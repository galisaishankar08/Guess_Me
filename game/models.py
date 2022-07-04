from django.db import models


# Create your models here.

class Signup(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)


class Signin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
