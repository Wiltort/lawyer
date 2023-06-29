from django.shortcuts import render
from .models import Service, Post, Banner

# Create your views here.
def index(request):
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
