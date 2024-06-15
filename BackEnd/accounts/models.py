from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_CHOICES = (
        ("F", "Female"),
        ("M", "Male")
    )


    address = models.TextField(blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              blank=True)
    phone = models.CharField(max_length=15,
                             blank=True)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
