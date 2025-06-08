from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('anime/<int:anime_id>/', views.detail, name='detail'),
    path('anime/<int:anime_id>/watch/<int:episode_num>/', views.watch, name='watch_episode'),
]