from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_img = models.ImageField(upload_to='profile_img/')
    stack = models.CharField(default="Stack", max_length=100)
    bio = models.TextField(default="Describe yourself here")

    def __str__(self):
        return f"{self.user.username} Profile"


