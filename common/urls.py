
from django.urls import path
from .import views

urlpatterns = [
    path('index', views.common_home),
     path('todo', views.common_todo),
      path('new', views.common_new),
      path('anim', views.common_anim),
      path('new1', views.common_new1),
      path('', views.common_new10),
    
]