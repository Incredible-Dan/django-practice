from django.contrib import admin
from posts.models import posts, comment

# Register your models here.
admin.site.register(posts)
admin.site.register(comment)