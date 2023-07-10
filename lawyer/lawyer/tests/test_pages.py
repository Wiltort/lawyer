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
    
    def test_new_record(self):
        '''Проверка возможности добавления записей'''
        self.client.logout()
        context = {'title': 'Test post#1', 'text': 'Пост гостя'}
        self.client.post(reverse('new_post'), context, follow=True)
        response = self.client.get(reverse('posts'))
        self.assertNotContains(response, text='Test post#1', msg_prefix='Гость создал пост!')
        self.client.force_login(self.user)
        context['title']='Test post#2'
        self.client.post(reverse('new_post'),context, follow=True)
        response = self.client.get(reverse('posts'))
        self.assertNotContains(response, text='Test post#2', msg_prefix='Юзер создал пост!')
        self.client.force_login(self.admin)
        context['title']='Test post#3'
        self.client.post(reverse('new_post'),context, follow=True)
        response = self.client.get(reverse('posts'))
        self.assertContains(response, text='Test post#3', msg_prefix='admin не создал пост!')

    #def test_edit_records(self):
        '''Проверка возможности редактирования записей'''

class Test_404(TestCase):
    def setUp(self):
        self.client = Client()
    def test_page_not_found(self):
        response = self.client.get('/1/1/')
        self.assertEqual(response.status_code, 404)