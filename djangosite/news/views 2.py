from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category
# Create your views here.

def index(request):
    news = News.objects.all() # Указали в админке сортировку в обратном порядке, теперь здесь можно не указывать
    context = {
        'news': news,
        'title': 'NEWS',
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category':category})
