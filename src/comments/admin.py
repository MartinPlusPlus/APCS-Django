from django.contrib import admin

# Register your models here.
from src.comments.models import Comment
from src.comments.models import Post

admin.site.register(Comment)
admin.site.register(Post)
