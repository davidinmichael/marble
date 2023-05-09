from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
# This is a signal handler function that listens to the post_save signal sent
# by the User model. Whenever a User instance is saved (either created or updated),
# this function checks if the instance is newly created, and if so, creates a
# corresponding Profile instance by calling the create() method of the Profile model.

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_profile, sender=User)

# This is another signal handler function that listens to the post_save signal
# sent by the User model. Whenever a User instance is save
# (either created or updated), this function simply saves the corresponding
# Profile instance by calling the save() method of the Profile model.
