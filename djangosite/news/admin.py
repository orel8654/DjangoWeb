from django.contrib import admin
from .models import News
from .models import Category
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creat_at', 'update_at', 'published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('published',) #Это кортеж, запятая обязательна иначе была бы строка
    list_filter = ('published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',) #Это кортеж, запятая обязательна иначе была бы строка

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
