from django.shortcuts import render
from django.urls import path, include, reverse, resolvers

from rest_framework import generics, permissions
from .serializers import PostsSerializers
from .models import Posts


# Create your views here.
class PostsViewSet(generics.ListCreateAPIView):
    # http_method_names = ['get']   # Allowed Methods
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def index(request):
    return render(request, 'index.html')