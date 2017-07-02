from django.test import TestCase, TransactionTestCase
from . import views
from django.test import Client
from freezegun import freeze_time
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import resolve


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
        self.assertRedirects(respond, '/accounting/')

    def test_redirect_for_unauthenticated_user_works(self):
        response = self.c.get('/accounting/')
        self.assertRedirects(response, '/?next=/accounting/')

    def test_redirect_works_for_bad_auth(self):
        respond = self.c.post('/', {'username': 'hiren', 'password': 'bad pass'})
        self.assertRedirects(respond, '/')

    def test_view_returns_correct_template(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'login.html')

    def test_authenticated_user_redirect_to_the_app(self):
        self.c.login(username='hiren', password='password')
        response = self.c.get('/', follow=True)
        self.assertRedirects(response, '/accounting/')