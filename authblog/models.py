from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    description = models.TextField(max_length=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'Commented by {self.author} on {self.blog}'