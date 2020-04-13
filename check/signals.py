from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Fluffy


@receiver(post_save, sender=Fluffy)
def announce_post_save(sender, instance, created, **kwargs):
    # punting to helper function to make it easy to patch with `unittest.mock.patch`
    # https://stackoverflow.com/a/44009903/11413244
    _announce_post_save(sender, instance, created, **kwargs)


def _announce_post_save(sender, instance, created, **kwargs):
    pass


@receiver(pre_save, sender=Fluffy)
def announce_pre_save(sender, instance, **kwargs):
    # punting to helper function to make it easy to patch with `unittest.mock.patch`
    # https://stackoverflow.com/a/44009903/11413244
    _announce_pre_save(sender, instance, **kwargs)


def _announce_pre_save(sender, instance, **kwargs):
    pass
