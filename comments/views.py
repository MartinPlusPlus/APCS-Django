from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from django.shortcuts import redirect

'''
# Lets us see what was submitted to the database
@api_view(['POST'])
def add_comment(request):
    # Make a serializer with the JSON from the request
    serializer = CommentSerializer(data=request.data)
    # Checks that the JSON has the right fields
    if serializer.is_valid():
        # Saves the object to the database
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

# Displays comments
def blog_post(request):
    if request.POST:
        # Make a serializer with the JSON from the request
        serializer = CommentSerializer(data=request.POST)
        # Checks that the JSON has the right fields
        if serializer.is_valid():
            # Saves the object to the database
            serializer.save()
            return redirect("/")

    # Get all the comments
    comments = Comment.objects.all()
    # Convert JSON to Python

    # Render HTML for the post
    return render(request, template_name="index.html", context={'comments': comments})
