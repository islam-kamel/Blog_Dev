from django.contrib.auth.models import User
from django.test import TestCase
from blog_api.models import Tags, Comments, Posts


class PostsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin')
        self.tags = Tags.objects.create(type='test')
        self.posts = Posts.objects.create(post_title='Test Case title', post_content='Test Case Post Content',
                                          created_by_id=1,
                                          tags_id=1)
        self.comment = Comments.objects.create(comment='Test', add_by_id=1, post_id_id=1)

    def test_posts_can_create(self):
        self.assertEqual(str(self.tags), 'test')
        self.assertEqual(self.user.username, 'admin')
        self.assertEqual(str(self.posts), 'Test Case title')
        self.assertEqual(str(self.comment), 'Test - admin - Test Case title')
