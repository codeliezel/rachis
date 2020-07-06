from django.db import models
from django.contrib.postgres.fields import ArrayField

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=10) 
    tags = ArrayField(
        models.CharField(max_length=300),
        blank=True, default=list, null=False)
    snippet_one = models.ImageField(default="snippet1.png", null=True, upload_to= 'snippets/%Y/%m/%D/')
    snippet_two = models.ImageField(default="snippet2.png", null=True, upload_to= 'snippets/%Y/%m/%D/')
    snippet_three = models.ImageField(default="snippet3.png", null=True, upload_to= 'snippets/%Y/%m/%D/')
    video_file = models.FileField(blank=True, null=True, upload_to= 'clips/%Y/%m/%D/')
    link = models.URLField(blank=True, max_length=200, default="url", null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
