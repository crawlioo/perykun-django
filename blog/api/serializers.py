from rest_framework.serializers import ModelSerializer

from blog.models import Blog


class BlogSerializers(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
