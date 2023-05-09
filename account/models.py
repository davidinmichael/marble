from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_img = models.ImageField(upload_to='profile_img/')

    def __str__(self):
        return f"{self.user.username} Profile"
