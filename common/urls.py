
from django.urls import path
from .import views

urlpatterns = [
    path('index', views.common_home),
     path('todo', views.common_todo),
      path('new', views.common_new),
      path('', views.common_anim),
    
]