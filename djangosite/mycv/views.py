from django.shortcuts import render
from django.http import HttpResponse
from .models import cvClient


# Create your views here.

def index(request):
    return render(request, template_name='mycv/index.html')

