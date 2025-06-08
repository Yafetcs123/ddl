from django.contrib import admin
from .models import Anime, details, voice_over, Genre, Animenya

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('judul', 'judul_in_english', 'season', 'rating', 'tanggal_rilis')
    list_filter = ('season', 'rating')
    search_fields = ('judul', 'judul_in_english')
    filter_horizontal = ('genre',)
    
    fieldsets = (
        ('Informasi Dasar', {
            'fields': ('judul', 'judul_in_english', 'season', 'rating')
        }),
        ('Detail', {
            'fields': ('tanggal_rilis', 'poster', 'genre')
        }),
    )

@admin.register(details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('Judul', 'episode', 'sinopsis_short')  # Ganti Judul jadi anime
    list_filter = ('Judul', 'episode')  # Ganti Judul jadi anime
    search_fields = ('anime__judul', 'sinopsis')  # Ganti Judul__Judul jadi anime__judul
    filter_horizontal = ('voice_over',)
    
    def sinopsis_short(self, obj):
        return f"{obj.sinopsis[:50]}..." if len(obj.sinopsis) > 50 else obj.sinopsis
    sinopsis_short.short_description = 'Sinopsis'

@admin.register(voice_over)
class VoiceOverAdmin(admin.ModelAdmin):
    list_display = ('voice_over',)
    search_fields = ('voice_over',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)
    search_fields = ('genre',)

@admin.register(Animenya)
class AnimenyaAdmin(admin.ModelAdmin):
    list_display = ('anime', 'episode', 'video')
    list_filter = ('anime', 'episode')
    search_fields = ('anime__judul',)
    ordering = ['anime', 'episode']

