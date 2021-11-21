from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from blog.forms import *

# Create your views here.
from .models import Blog

def homepage(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 2)
    page = request.GET.get("page")
    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        blog_page = paginator.page(1)
    except EmptyPage:
        blog_page = paginator.page(paginator.num_pages)

    return render(request, "blog/blog_list.html", context={"blog_list": blog_page, 'page': page})


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


def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(
                request, "accounts/register_done.html", context={"forms": user_form}
            )

    else:
        user_form = RegisterForm()
    return render(request, "accounts/register.html", context={"forms": user_form})

@login_required
def add_article(request):
    if request.method == "POST":
        blog_forms = BlogForms(request.POST)
        if blog_forms.is_valid():
            blog = blog_forms.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect("blog_list")
    else:
        blog_forms = BlogForms()
    return render(request, "blog/add.html", context={"blog": blog_forms})


@login_required
def update_article(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = BlogEditForms(request.POST or None, instance=blog)

    if form.is_valid():
        form.save()
        return redirect("blog_list")
    else:
        return render(request, "blog/update.html", context={"forms": form})

@login_required
def delete_article(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()
    return redirect("blog_list")
