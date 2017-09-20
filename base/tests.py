from django.test import TestCase, TransactionTestCase
from . import views
from django.test import Client
from freezegun import freeze_time
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import resolve
from django.urls import reverse


class LoginViewTest(TestCase):
    """
    Test for authentication
    """

    def setUp(self):
        User.objects.create_user('hiren', 'a@b.com', 'password')
        self.c = Client()

    def test_login_url_resolves_to_login_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.login)

    def test_auth(self):
        respond = self.c.post('/', {'username': 'hiren', 'password': 'password'})
        self.assertRedirects(respond, reverse('unlock'))

    def test_redirect_for_unauthenticated_user_works(self):
        response = self.c.get(reverse('dashboard'))
        self.assertRedirects(response, '/?next=' + reverse('dashboard'))

#     def test_redirect_works_for_bad_auth(self):
#         respond = self.c.post('/', {'username': 'hiren', 'password': 'bad pass'})
#         self.assertRedirects(respond, '/')
#
#     def test_view_returns_correct_template(self):
#         response = self.c.get('/')
#         self.assertTemplateUsed(response, 'base/login.html')
#
#     def test_authenticated_user_redirect_to_the_app(self):
#         self.c.login(username='hiren', password='password')
#         response = self.c.get('/', follow=True)
#         self.assertRedirects(response, '/accounting/dashboard/')
#
#
# class RegisterViewTest(TestCase):
#
#     def setUp(self):
#         User.objects.create_user('hiren', 'a@b.com', 'password')
#         self.c = Client()
#
#     def test_login_url_resolves_to_login_view(self):
#         found = resolve('/register/')
#         self.assertEqual(found.func, views.register)
#
#     def test_view_returns_correct_template(self):
#         response = self.c.get('/register/')
#         self.assertTemplateUsed(response, 'base/sign_up.html')
#
#     def test_redirect_for_authenticated_user_works(self):
#         self.c.login(username='hiren', password='password')
#         response = self.c.get('/register/')
#         self.assertRedirects(response, '/accounting/dashboard/')
#
#     def test_registration(self):
#         self.c.post('/register/', {'username': 'bunny', 'password': 'pass',
#                                    'email': 'meow@meow.com', 'confirm_password': 'pass'})
#         self.assertEqual(User.objects.count(), 2)
#
#
