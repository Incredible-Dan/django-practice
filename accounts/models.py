from django.db import models
# from accounts.models import owner

# Create your models here.


class owner(models.Model):
    username = models.CharField(max_length=20, unique= True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(default='bear.png')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username