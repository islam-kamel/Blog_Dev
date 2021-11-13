from django.urls import path, include, reverse, resolvers
from blog_api import views

# Assigned Global App Name
app_name = 'blog_apis'

# Url Getaway
urlpatterns = [
    path('', views.index, name='api_dec'),
    path('posts/', views.PostsList.as_view(), name='posts_api'),
    path('posts/<slug:slug>-<int:pk>', views.PostDetails.as_view(), name='post_detail'),
    path('create/', views.PostPost.as_view()),
    path('tags/', views.GetTags.as_view(), name='get_tags')

]
