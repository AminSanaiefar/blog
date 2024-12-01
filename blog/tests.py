from django.test import TestCase
from .models import BlogPost
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post = BlogPost.objects.create(
            title='post',
            text='this is description of post',
            status=BlogPost.STATUS_CHOICES[0][0],  # published
            author=cls.user,
        )
        cls.post2 = BlogPost.objects.create(
            title='post2',
            text='this is description of post2',
            status=BlogPost.STATUS_CHOICES[1][0],  # draft
            author=cls.user,
        )
    # def setUp(self):
    #     self.user = User.objects.create(username='user1')
    #     self.post = BlogPost.objects.create(
    #         title='post',
    #         text='this is description of post',
    #         status=BlogPost.STATUS_CHOICES[0][0],  # published
    #         author=self.user,
    #     )
    #     self.post2 = BlogPost.objects.create(
    #         title='post2',
    #         text='this is description of post2',
    #         status=BlogPost.STATUS_CHOICES[1][0],  # draft
    #         author=self.user,
    #     )

    def test_post_model_str(self):
        self.assertEqual(str(self.post), f'{self.post.author.username}: {self.post.title}')

    def test_post_list_url(self):
        # Check if the url path is changed
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        # Check if the name in the Url File For Path changed
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url(self):
        # Check if the url path is changed
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_show_post_title_in_list_page(self):
        # Check if the created post is showed on the post_list template
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post.title)

    def test_post_details_on_blog_detail(self):
        # Check if post detail showed on the post_detail template
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)

    def test_draft_post_not_show_in_post_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post.title)
        self.assertNotContains(response, self.post2.title)

    def test_create_view(self):
        response = self.client.post(reverse('create_post'), {
            'title': 'some title',
            'text': 'some text',
            'status': 'pub',
            'author': self.user.id
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, 'some title')
        self.assertEqual(BlogPost.objects.last().text, 'some text')

    def test_post_update_view(self):
        response = self.client.post(reverse('update_post', args=[self.post2.id]), {
            'title': 'updated title',
            'text': 'updated text',
            'status': 'pub',
            'author': self.user.id
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, 'updated title')
        self.assertEqual(BlogPost.objects.last().text, 'updated text')

    def test_post_delete_view(self):
        pk = self.post2.id
        response = self.client.post(reverse('delete_post', args=[self.post2.id]),)
        self.assertEqual(response.status_code, 302)