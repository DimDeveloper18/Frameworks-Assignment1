from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Comment

# Create your tests here.

class CommentTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.comment = Comment.objects.create(
            comwriter=cls.user,
            comname='Test Comment',
            comtext='This is test for comment'
        )

    def test_comtext(self):
        comment = Comment.objects.get(id=1)
        expected_comwriter = f'{comment.comwriter}'
        expected_comname = f'{comment.comname}'
        expected_comtext = f'{comment.comtext}'
        self.assertEqual(expected_comwriter, 'testuser')
        self.assertEqual(expected_comname, 'Test Comment')
        self.assertEqual(expected_comtext, 'This is test for comment')

    def test_comment_str(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(str(comment), comment.comname)

    def test_get_absolute_url(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.get_absolute_url(), reverse('products_store-comment-detail', args=[comment.id]))

class CommentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.comment = Comment.objects.create(
            comwriter=self.user,
            comname='Test Comment',
            comtext='This is test for comment'
        )

    def test_comment_list(self):
        url = reverse('products_store-tools')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)