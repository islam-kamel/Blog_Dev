from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tags(models.Model):
    type = models.CharField(max_length=100, help_text='Enter Post Tags Ex. Python, React.js')


class Comments(models.Model):
    comment = models.TextField()
    add_date = models.DateTimeField(auto_now_add=timezone.now())
    add_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Posts(models.Model):
    post_title = models.CharField(max_length=250)
    post_content = models.TextField()
    created_data = models.DateTimeField(auto_now_add=timezone.now())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.PROTECT)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
