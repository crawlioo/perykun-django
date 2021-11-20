from django.shortcuts import render

# Create your views here.
from .models import Blog

def homepage(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog_list.html', context={'content': blog})
