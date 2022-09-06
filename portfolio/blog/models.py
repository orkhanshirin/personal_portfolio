from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images/")
    publish_time = models.TimeField(auto_now=True)
    url = models.URLField(blank=True)
