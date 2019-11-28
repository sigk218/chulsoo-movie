from rest_framework import serializers
from .models import Actor, Director, Genre, Movie, Rating
from accounts.serializers import UserSerializer

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'peopleNm', 'movies',)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'peopleNm', 'movies',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genreNm', 'movies',)


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    like_user = UserSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'link', 'image', 'subtitle', 'pubDate', 'userRating', 'description', 'genres', 'actors', 'directors', 'youtube_price', 'youtube_link', 'naver_price', 'naver_link', 'like_user')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'content', 'score', 'user', 'movie',)
