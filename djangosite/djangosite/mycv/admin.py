from django.contrib import admin
from .models import cvClient
# Register your models here.

class cvClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'phone_number', 'city', 'diskription', 'time_guest')

admin.site.register(cvClient, cvClientAdmin)