from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Link to User model

    def __str__(self):
        return self.title