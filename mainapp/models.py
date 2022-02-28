from django.db import models

from mainapp.baseUser import CustomUser

class User(CustomUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email