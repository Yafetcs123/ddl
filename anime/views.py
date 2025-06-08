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
    animes = Anime.objects.all()
    
    # Filter jika ada keyword search
    if keyword:
        anim_query = animes.filter(judul__icontains=keyword)
    
    # Urutkan hasil
    animes = animes.order_by('judul')
    
    context = {
        'animes': animes,
        'keyword': keyword  # Kirim keyword ke template untuk ditampilkan kembali
    }
    return render(request, 'home.html', context)

def detail(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    detail_obj = details.objects.filter(Judul=anime).first()
    
    # Group karakter berdasarkan nama
    characters = {}
    for char in anime.characters.all():
        if char.nama not in characters:
            characters[char.nama] = []
        characters[char.nama].append(char)
    
    context = {
        'anime': anime,
        'detail': detail_obj,
        'characters': characters,  # Kirim karakter yang sudah dikelompokkan
        'genres': anime.genre.all(),
        'episodes': Animenya.objects.filter(anime=anime).order_by('episode')
    }
    return render(request, 'detail.html', context)

def watch(request, anime_id, episode_num):
    anime = get_object_or_404(Anime, id=anime_id)
    episode = get_object_or_404(Animenya, anime=anime, episode=episode_num)
    
    return render(request, 'anime.html', {
        'anime': anime,
        'episode': episode
    })