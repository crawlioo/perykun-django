from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from blog.models import Blog
from .serializers import BlogSerializers


@csrf_exempt
def api_blog_list(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = BlogSerializers(blog, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializers(data=data)

        # validate the serializer
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
