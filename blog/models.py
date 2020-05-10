from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # This function is used when new post create and after new post create then you redirect to home page
    # this function is used for redirect after post create
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

