from django.contrib import admin
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display=('title','date_created','author')


# Register your models here.
from .models import Post 
admin.site.register(Post,PostAdmin)