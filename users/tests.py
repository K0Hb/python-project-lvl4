from django.test import TestCase
from users.models import User
from status.models import Status
from django.urls import reverse
from tasks.models import Task
from django.db.models import ProtectedError


class UserTest(TestCase):

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
