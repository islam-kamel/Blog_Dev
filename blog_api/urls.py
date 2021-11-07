from django.urls import path, include
from blog_api import views

# Assigned Global App Name
app_name = 'blog_APIs'

# Url Getaway
urlpatterns = [
    path('posts', views.PostsViewSet.as_view(), name='posts_api')
]
