from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions, mixins, status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Posts, Tags
from .serializers import PostsSerializers, PostsCRUD, TagsSerializer


# Class Based View 'POST' and 'Get'

class PostsList(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostsSerializers
    queryset = Posts.objects.all()

    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializers(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        { "tags":[1,2], "post_title": "test serializer", "post_content": "test serializer"}
        """
        request.data['created_by'] = request.user.pk
        for id in request.data['tags']:
            if not Tags.objects.filter(pk=id).exists():
                # Tags.objects.create()
                return Response(id)

        serializer = PostsSerializers(data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetails(APIView):
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def get_object(slug):
        try:
            post = get_object_or_404(Posts, slug=slug)
            return post
        except Posts.DoesNotExist:
            raise Http404('Not Find Post')

    def get(self, request, pk, slug):
        post = self.get_object(slug)
        serializer = PostsSerializers(post)
        return Response(serializer.data)


class PostPost(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsCRUD

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class GetTags(generics.ListAPIView):
    serializer_class = TagsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        try:
            values = set(x.strip().lower() for x in self.request.query_params['tags'].split(','))
            print(values)
            for tag in values:
                result = Tags.objects.filter(type__startswith=tag)
            return result

        except KeyError:
            raise Http404(status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, 'index.html')
