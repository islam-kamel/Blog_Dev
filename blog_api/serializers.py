from rest_framework import serializers

from blog_api.models import Posts


class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['post_title', 'post_content', 'created_by', 'created_data', 'tags']
