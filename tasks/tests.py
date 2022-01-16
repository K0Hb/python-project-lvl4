from django.test import TestCase
from tasks.models import Task
from users.models import User
from status.models import Status


class TaskTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username='lol1',
                                         password='12345')
        user1.save()
        status1 = Status.objects.create(name='TestStatus1')
        status1.save()
        task1 = Task.objects.create(
            name='Down',
            description='Ou!',
            status=status1,
            creator=user1,
            executor=user1,
        )
        task1.save()

    def test_task(self):
        task = Task.objects.get(id=1)
        self.assertTrue(isinstance(task, Task))
        max_length = task._meta.get_field('name').max_length
        self.assertEquals(max_length, 75)
        task.name = 'Down'
        name = task.__str__()
        self.assertEquals(name, 'Down')
        assert task.description == 'Ou!'
        task.description = 'text'
        assert task.description == 'text'
