from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class blog_article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name="blog_posts",on_delete=models.CASCADE)

    class Meta:
        ordering = ("-publish",)

    def _str_(self):
        return self.title
