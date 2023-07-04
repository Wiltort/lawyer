from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()
# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField(null = True, blank=True)
    service = models.ForeignKey('Service', null=True, blank=True, 
                                on_delete=models.DO_NOTHING, 
                                related_name='clients')
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Review(models.Model):
    text = models.TextField(null = False, blank= False, verbose_name='текст')
    pub_date = models.DateTimeField(
        auto_now_add = True, 
        db_index=True, 
        verbose_name='дата публикации'
    )
    user = models.ForeignKey(
        User, 
        on_delete = models.SET('DELETED'),
        related_name='reviews', 
        verbose_name='автор отзыва'
    )
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Group(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, 
                             blank=False, verbose_name='название')
    class Meta:
        verbose_name = 'Группа услуг'
        verbose_name_plural = 'Группы услуг'
    def __str__(self):
        return self.title

class Service(models.Model):
    PERS = {
        ('n', 'Физическое лицо'),
        ('l', 'Юридическое лицо'),
    }
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='название')
    pers = models.CharField(max_length=1, choices=PERS, verbose_name='юр/физ лицо')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, 
                              related_name='services', verbose_name='группа услуг')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(null=False, blank=False, verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='posts', blank=True, null=True, verbose_name='Изображение')
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.SET('DELETED'),related_name='comments', verbose_name='Автор коммента')
    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'

class Banner(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название баннера')
    image = models.ImageField(upload_to = 'banners', blank = False, null = False, verbose_name='Изображение')
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'      
