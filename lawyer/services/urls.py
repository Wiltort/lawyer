from django.urls import path
from . import views

urlpatterns = [
    path('services/<int:pk>/', views.ServiceView.as_view(), name = 'service'),
    path('services/<int:pk>/new-client/', views.NewClient, name = 'new-client'),
    path('', views.index, name='index'),
    path("new-post/", views.new_post, name = "new_post"),
    path("posts/", views.posts, name = "posts"),
    path("posts/<int:post_id>/", views.post_view, name="post"),
    path("posts/<int:post_id>/edit/",views.post_edit, name="post_edit"),
    path("posts/<int:post_id>/comment/", views.add_comment, name="add_comment"),
]
