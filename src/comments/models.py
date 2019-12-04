from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    text = models.TextField()
    author = models.CharField(max_length=255)

# Create your models here.
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    name = models.CharField(max_length=100)

    _post = models.ForeignKey(to=Post, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.created.strftime("%m/%d/%Y") + " " + self.name
