from django.shortcuts import render

from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by("-publish_time")
    return render(request, "blog/all_blogs.html", {"blogs": blogs})
