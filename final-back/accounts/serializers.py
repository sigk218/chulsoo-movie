from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..movies.serializers import RatingSerializer

class UserSerializer(serializers.ModelSerializer):
    rating_set = RatingSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'rating_set',)