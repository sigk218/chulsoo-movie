from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genreNm = models.CharField(max_length=50)

class Actor(models.Model):
    peopleNm = models.CharField(max_length=30)
    peopleNmEn= models.CharField(max_length=30)
    
class Director(models.Model):
    peopleNm = models.CharField(max_length=30)
    peopleNmEn= models.CharField(max_length=30)

class Movie(models.Model):
    title = models.CharField(max_length=150)
    link = models.TextField()
    image = models.TextField()
    subtitle = models.CharField(max_length=150)
    pubDate = models.DateField()
    userRating = models.FloatField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')

class Rating(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

