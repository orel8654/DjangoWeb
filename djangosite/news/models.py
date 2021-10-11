from django.db import models
from django.urls import reverse
# Create your models here.
#SQLlite table
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название') #Created field text
    content = models.TextField(blank=True, verbose_name='Контент') #Created field discription news, blank=True it's mean field can be empty
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') #Created fied date-time when news added o site and after not changed
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления') #Created field date-time when news updates and writing new date-time
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True) #Created field sorted by Year, month, day
    published = models.BooleanField(default=True, verbose_name='Статус') #Created filed true or false
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self): #Метод, для того чтобы пердать в базе данных строку а не объект
        return self.title #Действует на title, можно что то еще

    class Meta:
        verbose_name = "Новость" #Вербовка имени единственного числа
        verbose_name_plural = 'Новости' #Вербовка имени множественного числа
        ordering = ['-creat_at', 'title'] #Сортировка сначала по дате если одинаковы то по title

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('cat', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
