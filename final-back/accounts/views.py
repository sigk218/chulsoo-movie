from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response(status=400)


@api_view(['GET', 'PUT','DELETE'])
def detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        username = user.username
        user.delete()
        return Response({
            'message': f'유저 {username}이 정상적으로 삭제되었습니다.'
        })
    elif request.method == 'PUT':
        # body 정보를 보낼 때 username, is_active 까지 보내주어야 됨.
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=400)


@api_view(['POST'])
def follow(request, follower_pk, following_pk):
    follower = get_object_or_404(get_user_model(), pk=follower_pk)
    following = get_object_or_404(get_user_model(), pk=following_pk)
    if request.method == 'POST':
        if not following.followers.filter(pk=follower_pk):
            following.followers.add(follower)
            return Response({
                'message': f'{follower.username}님 {following.username} 팔로우 완료'
            })
        else:
            following.followers.remove(follower)
            return Response({
                'message': f'{follower.username}님 {following.username} 팔로우 취소'
            })
    return Response(status=400)