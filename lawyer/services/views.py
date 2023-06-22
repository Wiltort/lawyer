from django.shortcuts import render
from .models import Service, Post

# Create your views here.
def index(request):
    srv_list = Service.objects.all()
    last_news = Post.objects.order_by('-pub_date')[:5]
    context = {'srv_list': srv_list, 'last_news': last_news}
    return render(request, 'index.html', context)
