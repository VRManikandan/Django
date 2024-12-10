from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        print(self.title)
    
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post_title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField()

    def __str__ (self):
        return self.post_title