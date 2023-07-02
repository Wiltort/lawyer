from django.urls import path
from . import views

urlpatterns = [
    path('services/<int:pk>/', views.ServiceView.as_view(), name = 'service'),
    path('services/<int:pk>/new-client/', views.NewClient, name = 'new-client'),
    path('', views.index, name='index'),
]
