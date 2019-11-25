from django.contrib import admin

# Register your models here.
from src.comments.models import Comment

admin.site.register(Comment)
