from django.contrib import admin
from .models import Anime, details, voice_over, Genre, Animenya, Studio,  Character

class CharacterInline(admin.TabularInline):
    model = Character
    extra = 16  # Jumlah form foto tambahan
    fields = ('nama', 'foto', 'detail')  # Field yang ditampilkan
@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('judul', 'judul_in_english', 'season', 'rating', 'tanggal_rilis')
    list_filter = ('season', 'rating')
    search_fields = ('judul', 'judul_in_english')
    filter_horizontal = ('genre',)
    multiupload_list = False
    multiupload_form = True
    inlines = [CharacterInline]
    
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


admin.site.register(Studio)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('nama', 'anime', 'detail')  # Kolom yang ditampilkan di list view
    list_filter = ('anime',)  # Filter berdasarkan anime
    search_fields = ('nama',)  # Pencarian berdasarkan nama karakter
    raw_id_fields = ('anime', 'detail')  # Memudahkan pencarian relasi

    # Optional: Tampilkan form yang lebih rapi
    fieldsets = (
        ('Informasi Karakter', {
            'fields': ('nama', 'foto')
        }),
        ('Relasi', {
            'fields': ('anime', 'detail')
        }),
    )


    # Tambahkan method untuk handle multiupload
def process_uploaded_file(self, uploaded_file):
        # Contoh: Otomatis buat karakter baru dari file yang diupload
        character = Character.objects.create(
            nama=uploaded_file.name.split('.')[0],
            foto=uploaded_file,
            anime=self.instance
        )
        return {
            'url': character.foto.url,
            'thumbnail_url': character.foto.url,
            'id': character.id,
            'name': character.nama
        }