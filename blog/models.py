from django.db import models
from django.contrib.auth.models import User

class BlogType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    description = models.CharField(max_length=101, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        