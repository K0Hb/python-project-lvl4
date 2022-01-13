from django.test import TestCase
from users.models import User
from status.models import Status
from django.urls import reverse
from tasks.models import Task
from labels.models import Labels
from django.db.models import ProtectedError


class TaskTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username='lol1',
                                         password='12345')
        user1.save()
        user2 = User.objects.create_user(username='lol2',
                                         password='19911')
        user2.save()
        status1 = Status.objects.create(name='TestStatus1')
        status1.save()
        status2 = Status.objects.create(name='TestStatus2')
        status2.save()
        tag1 = Labels.objects.create(name='TestTag1')
        tag1.save()
        tag2 = Labels.objects.create(name='TestTag2')
        tag2.save()
        task1 = Task.objects.create(
            name='Down',
            description='Ou!',
            status=status1,
            creator=user1,
            executor=user2,
        )
        task2 = Task.objects.create(
            name='Down1',
            description='Ou1!',
            status=status1,
            creator=user2,
            executor=user2,
        )
        task1.save()
        task2.save()

    def test_view_url(self):
        url_list = ['', "/users/", "/login/",
                    "/users/create/", "/users/2/delete/", "/users/1/update/",
                    "/statuses/", "/statuses/create/", "/statuses/1/delete/",
                    "/tasks/", "/tasks/create/", "/tasks/1/delete/",
                    "/tasks/1/",
                    "/labels/", "/labels/create/", "/labels/1/delete/"]
        self.client.login(username='lol1', password='12345')
        for url in url_list:
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 200)

    def test_all_objects_in_list(self):
        url_and_list_pack = [
            ("users_page", "users_list"),
            ("labels", "labels_list"),
            ("statuses", "statuses_list"),
            ("tasks", "tasks_list"),
        ]
        self.client.login(username='lol1', password='12345')
        for url_name, iter_name in url_and_list_pack:
            resp_all = self.client.get(reverse(url_name))
            self.assertEqual(resp_all.status_code, 200)
            self.assertEqual(len(resp_all.context[iter_name]), 2)

    def test_status(self):
        task_status = Status.objects.get(id=1)
        self.assertTrue(isinstance(task_status, Status))
        max_length = task_status._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)
        task_status.name = 'test_name'
        name = task_status.__str__()
        self.assertEquals(name, 'test_name')

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

    def test_tag(self):
        tag = Labels.objects.get(id=1)
        self.assertTrue(isinstance(tag, Labels))
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_update_user(self):
        self.client.login(username='lol1', password='12345')
        response = self.client.post(reverse('update_user', args='1'), {
            'first_name': 'lol_new',
            'last_name': 'lol_f',
            'username': 'lol_test',
            'password1': '12345test',
            'password2': '12345test',
        }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual('lol_new', User.objects.get(pk=1).first_name)
        self.assertEqual('lol_test', User.objects.get(pk=1).username)

    def test__protect_delete_user(self):
        user_protect = User.objects.filter(pk=1)
        try:
            user_protect.delete()
        except ProtectedError:
            self.assertTrue(User.objects.get(pk=1))
