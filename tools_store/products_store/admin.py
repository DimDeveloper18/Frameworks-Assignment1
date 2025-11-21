from django.contrib import admin
from .models import Comment
from .models import User_profile

# Register your models here.

admin.site.register(Comment)
admin.site.register(User_profile)
