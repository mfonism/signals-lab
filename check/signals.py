from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Fluffy


@receiver(post_save, sender=Fluffy)
def announce_post(sender, instance, created, **kwargs):
    print("In POST_SAVE", end=" - ")
    if not created:
        print("already existing instance...")
        return
    print("new instance...")


@receiver(pre_save, sender=Fluffy)
def announce_pre(sender, instance, **kwargs):
    print("In PRE_SAVE...")
