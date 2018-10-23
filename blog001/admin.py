from django.contrib import admin
from .models import blog_article
# Register your models here.


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "publish")
    list_filter = ("publish",)
    search_fields = ("title", "body")
admin.site.register(blog_article, BlogArticlesAdmin)