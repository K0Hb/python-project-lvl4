from django.test import TestCase
from status.models import Status


class StatusTest(TestCase):

    def setUp(self):
        status1 = Status.objects.create(name='TestStatus1')
        status1.save()

    def test_status(self):
        task_status = Status.objects.get(id=1)
        self.assertTrue(isinstance(task_status, Status))
        max_length = task_status._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)
        task_status.name = 'test_name'
        name = task_status.__str__()
        self.assertEquals(name, 'test_name')
