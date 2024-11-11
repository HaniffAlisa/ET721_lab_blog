from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)          # Title of the blog post with a max length of 200 characters
    content = models.TextField()                      # Content of the blog post
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-sets to current date/time when created
    updated_at = models.DateTimeField(auto_now=True)      # Auto-updates to current date/time on save

    def __str__(self):
        return self.title