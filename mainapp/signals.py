from venv import create
from django.db.models.signals import post_save

from mainapp.models import UserProfile, User

def post_save_created_signal(sender, instance, created, **kwargs):
    # print(sender, instance, created)
    # print()
    # print(kwargs)
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(post_save_created_signal, sender=User)