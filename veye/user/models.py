from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=20, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email
