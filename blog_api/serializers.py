from rest_framework import serializers

from blog_api.models import Posts, Tags


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class PostsSerializers(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True, required=False, default='none')

    class Meta:
        model = Posts
        fields = '__all__'


class PostsCRUD(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
