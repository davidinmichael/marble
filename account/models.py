from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_img = models.ImageField(default="images/default.jpg", upload_to='profile_img/')
    stack = models.CharField(default="Stack", max_length=100)
    bio = models.TextField(default="Describe yourself here")

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_img.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300) # setting the desired size
            img.thumbnail(output_size)
            img.save(self.profile_img.path)


