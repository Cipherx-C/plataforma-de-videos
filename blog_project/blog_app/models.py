from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
