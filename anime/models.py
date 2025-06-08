from django.db import models

# Model untuk season choices (tetap sebagai IntegerChoices)
class season(models.IntegerChoices):
    season_1 = 1, 'Season 1'
    season_2 = 2, 'Season 2'
    season_3 = 3, 'Season 3'
    season_4 = 4, 'Season 4'

class Genre(models.Model):
    genre = models.CharField()
    
    def __str__(self):
        return self.genre

class Anime(models.Model):
    judul = models.CharField()
    judul_in_english = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    rating = models.IntegerField()
    tanggal_rilis = models.DateTimeField()
    poster = models.ImageField(upload_to='poster/')
    season = models.IntegerField(choices=season.choices)
    
    def __str__(self):
        return self.judul

class voice_over(models.Model):
    voice_over = models.CharField(max_length=255)
    foto_vc = models.ImageField(upload_to='voice_over')
    
    def __str__(self):
        return self.voice_over

class JumlahEpisode(models.IntegerChoices):
    Episode_1 = 1, 'Episode 1' 
    Episode_2 = 2, 'Episode 2' 
    Episode_3 = 3, 'Episode 3' 
    Episode_4 = 4, 'Episode 4' 
    Episode_5 = 5, 'Episode 5' 
    Episode_6 = 6, 'Episode 6' 
    Episode_7 = 7, 'Episode 7' 
    Episode_8 = 8, 'Episode 8' 
    Episode_9 = 9, 'Episode 9' 
    Episode_10 = 10, 'Episode 10' 
    Episode_11 = 11, 'Episode 11' 
    Episode_12 = 12, 'Episode 12' 
    Episode_13 = 13, 'Episode 13'

class Studio(models.Model):
    nama = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.nama

class details(models.Model):
    Judul = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='details_episodes')
    episode = models.IntegerField(choices=JumlahEpisode.choices)
    sinopsis = models.TextField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)
    judul_in_english = models.CharField(max_length=255)
    voice_over = models.ManyToManyField(voice_over)
    
    def __str__(self):
        return f"{self.Judul.judul} - Episode {self.get_episode_display()}"
class Animenya(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episodes')
    episode = models.IntegerField(choices=JumlahEpisode.choices)
    video = models.FileField(upload_to='anime')
    urls = models.URLField(max_length=200, null=True) 
    
    class Meta:
        ordering = ['episode']
        verbose_name_plural = 'Animenya'
    
    def __str__(self):
        return f"{self.anime.Judul} - Episode {self.get_episode_display()}"