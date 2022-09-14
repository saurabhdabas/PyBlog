from django.urls import path
from . import views 

urlpatterns = [
  path('posts/', views.posts, name='posts'),
  path('posts/<slug>', views.post, name='post'),
]