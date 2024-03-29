from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.urls import reverse

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    create_data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to="photos/",blank=True)
    
    
    
    def __str__(self) -> str:
        return self.title
    
    