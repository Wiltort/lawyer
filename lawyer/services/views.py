#from typing import Any, Dict
#from typing import Any, Dict, Optional, Type
#from django.forms.models import BaseModelForm
from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Post, Banner, Client
from django.views.generic.detail import DetailView
from .forms import ClientForm
from django.views.generic.edit import CreateView
from django.urls import reverse


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
            return redirect('index')
        context = {'form': form,}
        return render(request, 'new_client.html', context)
    form = ClientForm()
    return render(request, 'new_client.html', {'form': form,})

