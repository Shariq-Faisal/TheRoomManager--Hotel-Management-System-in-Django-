from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    role = models.CharField(max_length=50, default = 'Receptionist')


    def __str__(self):
        return self.username