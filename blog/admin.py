from django.contrib import admin
from .models import BlogPost

# Register your models here.
#for what you see on www.acquainted.site/admin. helps if i need to go into the back door for some reason


class BlogPostAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('title', 'header',)



admin.site.register(BlogPost, BlogPostAdmin)
