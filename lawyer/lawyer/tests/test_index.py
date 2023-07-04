from django.test import TestCase, Client
#import datetime as dt
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class IndexTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username = "sarah",
            email = "connor.s@skynet.com",
            password = "12345"
        )
        self.admin = User.objects.create_superuser(
            username = "t-1000",
            email = "1010001@skynet.com",
            password = "100010101"
        )
        
    def test_index(self):
        '''Проверка доступности страницы для разных пользователей'''
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200,msg='index page is not 200')
        self.assertContains(response, 'Инна', msg_prefix='В странице нет ИННА')
        self.client.force_login(self.user)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200,msg='index page is not 200')
        self.assertContains(response, 'Инна', msg_prefix='В странице нет ИННА')
        self.client.force_login(self.admin)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200,msg='index page is not 200')
        self.assertContains(response, 'Инна', msg_prefix='В странице нет ИННА')