from django.contrib import admin
from .models import*

# Register your models here.


# class BlogAdmin(admin.ModelAdmin):
#     class Media:
#         css = {
#             "all": ("css/main.css",)
#         }

#         js = ("js/blog.js",)


# admin.site.register(Blog, BlogAdmin)
admin.site.register(Blog)
admin.site.register(Contact)
