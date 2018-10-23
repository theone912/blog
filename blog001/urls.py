from django.conf.urls import url
from . import views

app_name='blog001'
urlpatterns = [
    url(r'^$', views.article_title, name="blog_title"),
]
