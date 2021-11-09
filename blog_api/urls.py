from django.urls import path, include, reverse, resolvers
from blog_api import views

# Assigned Global App Name
app_name = 'blog_apis'

# Url Getaway
urlpatterns = [
    path('', views.index, name='api_dec'),
    path('posts/', views.PostsViewSet.as_view(), name='posts_api')
]
