from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login

from blog.forms import LoginForm

# Create your views here.
from .models import Blog


def homepage(request):
    blog = Blog.objects.all()
    return render(request, "blog/blog_list.html", context={"blog_list": blog})


# blog detail
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, "blog/blog_detail.html", context={"content": blog})


# user login
def user_login(request):
    if request.method == "POST":
        forms = LoginForm(request.POST)

        if forms.is_valid():
            cleaned = forms.cleaned_data
            user = authenticate(
                request, username=cleaned["username"], password=cleaned["password"]
            )
            if user is not None:
                login(request, user)
                return HttpResponse("you are authenticate")

            else:
                return HttpResponse("Invalid Login")
    else:
        forms = LoginForm()

    return render(request, "accounts/login.html", context={"forms": forms})
