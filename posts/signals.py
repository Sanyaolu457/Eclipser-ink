from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import Participant
from .models import Profile

@receiver(post_save, sender=Participant)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Participant)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()