from django.contrib import admin
from . models import Post, PostImages, Tags


admin.site.register(Post)
admin.site.register(PostImages)
admin.site.register(Tags)