from django.test import TestCase
from main_page.models import CustomUser
from status.models import Status
from django.urls import reverse
from tasks.models import Task


class TaskTest(TestCase):

    def setUp(self):
        user1 = CustomUser.objects.create_user(username='lol1',
                                               password='12345',
                                               email='test@yandex.ru')
        user1.save()
        user2 = CustomUser.objects.create_user(username='lol2',
                                               password='19911',
                                               email='test_2@yandex.ru')
        user2.save()
        status = Status.objects.create(name='TestStatus')
        status.save()
        task = Task.objects.create(
            name='Go home',
            description='Faster!',
            status=status,
            creator=user1,
            executor=user2,
        )
        task.save()

    def test_user_login(self):
        self.client.login(username='lol1', password='12345')
        resp = self.client.get(reverse('statuses'))
        self.assertEqual(str(resp.context['user']), 'lol1')
        self.assertEqual(resp.status_code, 200)

    def test_status(self):
        task_status = Status.objects.get(id=1)
        self.assertTrue(isinstance(task_status, Status))
        max_length = task_status._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)
        task_status.name = 'test_name'
        name = task_status.__str__()
        self.assertEquals(name, 'test_name')
        task_status.delete()
        self.assertEqual(Status.objects.count(), 0)

    def test_task(self):
        task = Task.objects.get(id=1)
        self.assertTrue(isinstance(task, Task))
        max_length = task._meta.get_field('name').max_length
        self.assertEquals(max_length, 75)
        task.name = 'new_name'
        name = task.__str__()
        self.assertEquals(name, 'new_name')
        assert task.description == 'Faster!'
        task.description = 'blablabla'
        assert task.description == 'blablabla'
        task.delete()
        self.assertEqual(Task.objects.count(), 0)
