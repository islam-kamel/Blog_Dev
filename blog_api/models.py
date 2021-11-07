from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tags(models.Model):
    """
    Tags Table As Foreignkey Relationship
    """
    type = models.CharField(max_length=100, help_text='Enter Post Tags Ex. Python, React.js')

    def __str__(self):
        return self.type


class Posts(models.Model):
    """
    Posts Table with include Tags Table
    """
    post_title = models.CharField(max_length=250)
    post_content = models.TextField()
    created_data = models.DateTimeField(auto_now_add=timezone.now())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.PROTECT)

    def __str__(self):
        return self.post_title[:20]


class Comments(models.Model):
    """
    Comments Table As Foreignkey Relationship with Posts Table, Current User
    """
    comment = models.TextField()
    add_date = models.DateTimeField(auto_now_add=timezone.now())
    add_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment[:20]} - {User.objects.get(pk=self.add_by.pk)} - {Posts.objects.get(pk=self.post_id.pk)}'
