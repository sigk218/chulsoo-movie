from rest_framework import serializers
from .models import Actor, Director, Genre, Movie, Rating

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'peopleNm', 'peopleNmEn', 'movies',)

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'peopleNm', 'peopleNmEn', 'movies',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genreNm', 'movies',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'link', 'image', 'subtitle', 'pubDate', 'userRating', 'description', 'genre', 'actors', 'directors',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'content', 'score', 'user', 'movie',)
