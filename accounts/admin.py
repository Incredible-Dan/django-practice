from django.contrib import admin
from .models import owner


# Register your models here.
# do Admin .site.register(owner)


class owner_admin(admin.ModelAdmin):
    display = ('username', 'email', 'phone_number')


admin.site.register(owner, owner_admin)
