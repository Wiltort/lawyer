from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()
# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField(unique=True, null = True, blank=True)

class Review(models.Model):
    text = models.TextField(null = False, blank= False)
    pub_date = models.DateTimeField(auto_now_add = True, db_index=True)
    user = models.ForeignKey(User, on_delete = models.SET('DELETED'), related_name='reviews')

class Group(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)

class Service(models.Model):
    PERS = {
        ('n', 'Физическое лицо'),
        ('l', 'Юридическое лицо'),
    }
    title = models.CharField(max_length=50, null=False, blank=False)
    pers = models.CharField(max_length=1, choices=PERS)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='services')
    price = models.IntegerField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=False, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    #image = 
        

class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET('DELETED'),related_name='comments')\

