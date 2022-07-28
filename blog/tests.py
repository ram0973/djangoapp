from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post, Category


class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')

        test_user = get_user_model().objects.create_user(
            email='test@user.com', password='123456789')
        test_user.save()

        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt',
            content='Post Content', slug='post-title',
            author_id=1, status='published')
        test_post.save()

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test@user.com')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "django")
