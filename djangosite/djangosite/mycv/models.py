from django.db import models

# Create your models here.

class cvClient(models.Model):
    client_name = models.CharField(max_length=150, verbose_name='Имя')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    city = models.CharField(max_length=150, verbose_name='Город')
    diskription = models.TextField(blank=True, verbose_name='Пожелания')
    time_guest = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата записи')

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'Гостей'
        verbose_name_plural = 'Гость'
        ordering = ['-time_guest', 'client_name']
