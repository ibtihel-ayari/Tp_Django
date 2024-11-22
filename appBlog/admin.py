from django.contrib import admin

from appBlog.models import Author, BlogPost

# Register your models here.
admin.site.register(Author)
admin.site.register(BlogPost)