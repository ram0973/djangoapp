from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


class PostTests(APITestCase):

    def test_view_posts(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        """
        Ensure we can create a new Post object and view object.
        """
        self.test_category = Category.objects.create(name='django')
        self.test_user = get_user_model().objects.create_superuser(
            email='test@user.com', password='123456789')
        # self.test_user.is_staff = True

        self.client.login(email=self.test_user.email,
                          password='123456789')

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='django')
        self.test_user = get_user_model().objects.create_user(
            email='test@user.com', password='123456789')
        self.test_user2 = get_user_model().objects.create_user(
            email='test2@user.com', password='123456789')
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')

        client.login(email=self.test_user.email,
                     password='123456789')

        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
