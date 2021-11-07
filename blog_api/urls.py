from django.urls import path
from blog_api import views

# Assigned Global App Name
app_name = 'blog_APIs'

# Url Getaway
urlpatterns = [
    path('', views.index, name='home')
]
