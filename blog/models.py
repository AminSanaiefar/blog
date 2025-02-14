from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    def __str__(self):
        return f'{self.author.username}: {self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
