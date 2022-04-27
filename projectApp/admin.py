from django.contrib import admin
from .models import userInfo,genre,courses,comments

# Register your models here.
admin.site.register(userInfo)
admin.site.register(courses)
admin.site.register(genre)
admin.site.register(comments)