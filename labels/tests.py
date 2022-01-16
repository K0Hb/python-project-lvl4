from django.test import TestCase
from labels.models import Labels


class StatusTest(TestCase):

    def setUp(self):
        tag1 = Labels.objects.create(name='TestTag1')
        tag1.save()

    def test_tag(self):
        tag = Labels.objects.get(id=1)
        self.assertTrue(isinstance(tag, Labels))
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)
