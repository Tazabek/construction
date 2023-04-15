from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to= 'profile_image/'
    )

    def __str__(self) -> str:
        return self.username