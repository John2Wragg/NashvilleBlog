from django.contrib import admin
from pro1.models import Post, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

# Register our models to the admin site to allow for interaction. 
