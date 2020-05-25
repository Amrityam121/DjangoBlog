from django.db import models

# Create your models here.
class Post(models.Model):
    blog_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=70)
    author=models.CharField(max_length=50)
    content = models.CharField(max_length=2000)
    slug = models.CharField(max_length=50)
    timestamp = models.DateTimeField(blank=True)
    def __str__(self):
         return self.title
