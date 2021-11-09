from django.db import models

class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.title
