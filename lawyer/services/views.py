#from typing import Any, Dict
#from typing import Any, Dict, Optional, Type
#from django.forms.models import BaseModelForm
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Post, Banner, Client
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ClientForm, PostForm, CommentForm
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator


User = get_user_model()
# Create your views here.
def index(request):
    '''Главная страница, размещаем баннеры и услуги'''
    srv_list = Service.objects.all()
    srv_per_list = Service.objects.filter(pers = 'n')
    srv_jur_list = Service.objects.filter(pers = 'l')
    last_news = Post.objects.order_by('-pub_date')[:5]
    banners = Banner.objects.all()
    context = {
        'srv_list': srv_list,
        'srv_per_list': srv_per_list,
        'srv_jur_list': srv_jur_list,
        'last_news': last_news,
        'banners': banners,
        }
    return render(request, 'index.html', context)

class ServiceView(DetailView):
    model = Service
    template_name = 'service.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def NewClient(request, pk):
    srv = get_object_or_404(Service, pk = pk)
    if (request.method == 'POST'):
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit = False)
            client.service = srv
            client.save()
            send_mail(
                'Новый клиент',
                f'Новый клиент записался на услугу: {srv}.',
                'wiltort21@gmail.com',
                ['wiltort21@gmail.com'],
                fail_silently=False
            )

            return redirect('index')
        context = {'form': form, 'srv':srv}
        return render(request, 'new_client.html', context)
    form = ClientForm()
    return render(request, 'new_client.html', {'form': form,})

@permission_required('services.add_Post', raise_exception=True)
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, files=request.FILES or None)

        if form.is_valid():
            post = form.save(commit = False)
            #post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'new_post.html', {'form':form, 'Edit' : False})
    form = PostForm()
    return render(request, 'new_post.html', {'form':form, 'Edit': False})

def posts(request):
    #запрос к БД сортировка по убыванию и вывод всех
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list,10)
    #Разбиваем паджинатором по 10 постов
    page_number = request.GET.get('page')
    # variable in url with number of page
    page = paginator.get_page(page_number)
    if request.user.has_perm('services.change_Post'):
        perm = True
    else:
        perm = False
    return render(
        request,
        "posts.html",
        {'page': page, 'paginator': paginator, 'perm': perm}
        )

#class PostsView(ListView):
#    model=Post
#    ordering = "-pub_date"
#    template_name = 'posts.html'
#    paginate_by = 10
#    context_object_name = 'post_list'
    
def post_view(request, post_id):
        # тут тело функции
        post = get_object_or_404(Post, id = post_id)
        items = post.comments.all()
        form = CommentForm(instance=None)
        if request.user.has_perm('services.change_Post'):
            perm = True
        else:
            perm = False

        return render(
            request,
            'post.html',
            {'post': post, 'items': items, 'form': form, 'perm': perm}
            )

@permission_required('posts.edit_Post', raise_exception=False)
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    #form = PostForm(instance = post, initial=[{'group': 'post.group', 'text':'hjshdjshdsjhdsdhsjhjsh'}])
    
         #raise PermissionError("Вы не можете редактировать этот пост")
        # тут тело функции. Не забудьте проверить, 
        # что текущий пользователь — это автор записи.
        # В качестве шаблона страницы редактирования укажите шаблон создания новой записи
        # который вы создали раньше (вы могли назвать шаблон иначе)
    if (request.method == 'POST'):
        form = PostForm(request.POST, files=request.FILES or None, instance = post)
               
        if form.is_valid():
            post = form.save(commit = False)
            
            post.save()
            return redirect('post', post_id = post_id)
        return render(request, 'new_post.html', {'form':form, 'Edit': True, 'post':post})
    form = PostForm(instance=post)
    return render(request, 'new_post.html', {'form':form, 'Edit': True, 'post': post})

@login_required
def add_comment(request, post_id):
    
    post = get_object_or_404(Post, id = post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post', post_id)
        return render(
            request, 
            'post.html', 
            {'form':form, 'post_id' : post_id}
        )
    form = CommentForm()
    return render(
        request, 
        'post.html', 
        {'form':form, 'post_id': post_id}
    )

def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию, 
    # выводить её в шаблон пользователской страницы 404 мы не станем
    return render(
        request, 
        "misc/404.html", 
        {"path": request.path}, 
        status=404
    )

def server_error(request):
    return render(request, "misc/500.html", status=500)
