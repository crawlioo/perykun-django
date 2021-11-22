from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
        ordering = ['published']


    def __str__(self) -> str:
        return f'{self.title} - {self.published}'