from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Blog

def homepage(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog_list.html', context={'blog_list': blog})

# blog detail
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/blog_detail.html', context={'content': blog})