from unittest.mock import patch

from django.test import TestCase

from .models import Fluffy


class TestSignals(TestCase):
    @patch("check.signals._announce_post_save")
    def test_post_save_fired_on_instance_save(self, patched_handler):
        """
        Assert POST SAVE signal is fired on creating Fluffy model objects by
        instantiating the class and then calling `save()` on the instance.
        """
        f = Fluffy(name="Kintsugi")
        f.save()
        self.assertEqual(patched_handler.call_count, 1)

    @patch("check.signals._announce_post_save")
    def test_post_save_fired_on_objects_create(self, patched_handler):
        """
        Assert that POST SAVE signal is fired on creating Fluffy model objects by
        using the model's _objects_ manager's `create()` method.
        """
        Fluffy.objects.create(name="Kintsugi")
        self.assertEqual(patched_handler.call_count, 1)

    @patch("check.signals._announce_pre_save")
    def test_pre_save_fired_on_instance_save(self, patched_handler):
        """
        Assert PRE SAVE signal is fired on creating Fluffy model objects by
        instantiating the class and then calling `save()` on the instance.
        """
        f = Fluffy(name="Kintsugi")
        f.save()
        self.assertEqual(patched_handler.call_count, 1)

    @patch("check.signals._announce_pre_save")
    def test_pre_save_fired_on_objects_create(self, patched_handler):
        """
        Assert that PRE SAVE signal is fired on creating Fluffy model objects by
        using the model's _objects_ manager's `create()` method.
        """
        Fluffy.objects.create(name="Kintsugi")
        self.assertEqual(patched_handler.call_count, 1)
