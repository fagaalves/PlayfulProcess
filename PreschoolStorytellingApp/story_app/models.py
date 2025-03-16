from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='stories/images/')
    created_at = models.DateTimeField(auto_now_add=True)
