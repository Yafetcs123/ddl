from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ubah 'home/' menjadi '' untuk halaman utama
    path('list', views.list, name='list'),  # Ubah 'home/' menjadi '' untuk halaman utama
    path('anime/<int:anime_id>/', views.detail, name='anime_detail'),
    path('anime/<int:anime_id>/watch/<int:episode_num>/', views.watch, name='watch_episode'),
]