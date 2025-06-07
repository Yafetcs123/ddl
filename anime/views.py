from django.shortcuts import render, get_object_or_404
from .models import Anime, details, Animenya, Genre

def list(request):
    # Ambil semua anime, urutkan berdasarkan judul
    animes = Anime.objects.all().order_by('judul')
    
    return render(request, 'list.html', {'animes': animes})
def home(request):
    # Ambil parameter search dari URL
    keyword = request.GET.get('q', '').strip()
    
    # Query dasar untuk semua anime
    anim = Anime.objects.all()
    
    # Filter jika ada keyword search
    if keyword:
        anim_query = anim.filter(judul__icontains=keyword)
    
    # Urutkan hasil
    anim = anim.order_by('judul')
    
    context = {
        'anime': anim,
        'keyword': keyword  # Kirim keyword ke template untuk ditampilkan kembali
    }
    return render(request, 'home.html', context)

def detail(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    
    genres = anime.genre.all()
    episodes = Animenya.objects.filter(anime=anime).order_by('episode')
    detail = details.objects.filter(Judul=anime).first()
    
    return render(request, 'detail.html', {
        'anime': anime,
        'genres': genres,
        'episodes': episodes,
        'detail': detail
    })

def watch(request, anime_id, episode_num):
    anime = get_object_or_404(Anime, id=anime_id)
    episode = get_object_or_404(Animenya, anime=anime, episode=episode_num)
    
    return render(request, 'anime.html', {
        'anime': anime,
        'episode': episode
    })