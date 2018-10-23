from django.shortcuts import render
from blog001.models import blog_article

# Create your views here.
def article_title(request):
    blogs = blog_article.objects.all()
    return render(request, "blog001/title.html", {"blogs":blogs})
