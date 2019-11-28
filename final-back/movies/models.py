from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genreNm = models.CharField(max_length=50)

class Actor(models.Model):
    peopleNm = models.CharField(max_length=30)
    
class Director(models.Model):
    peopleNm = models.CharField(max_length=30)

class Movie(models.Model):
    title = models.CharField(max_length=150)
    link = models.TextField()
    image = models.TextField()
    subtitle = models.CharField(max_length=150, blank=True)
    pubDate = models.IntegerField()
    userRating = models.FloatField()
    description = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)
    directors = models.ManyToManyField(Director, related_name='movies')
    youtube_price = models.CharField(max_length=150, blank=True)
    youtube_link = models.TextField(blank=True)
    naver_price = models.CharField(max_length=150, blank=True)
    naver_link =  models.TextField(blank=True)

class Rating(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

