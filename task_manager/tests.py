from django.test import TestCase
from users.models import User
from django.urls import reverse
from tasks.models import Task
from labels.models import Labels
from status.models import Status


class ViewTest(TestCase):

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
        self.client.login(username='lol1', password='12345')
        url_list = ['', "/users/", "/login/",
                    "/users/create/", "/users/1/delete/", "/users/1/update/",
                    "/statuses/", "/statuses/create/", "/statuses/1/delete/",
                    "/tasks/", "/tasks/create/", "/tasks/1/delete/",
                    "/tasks/1/",
                    "/labels/", "/labels/create/", "/labels/1/delete/"]
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
