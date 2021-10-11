from django.shortcuts import render
from django.http import HttpResponse
from .forms import DromParser
# Create your views here.

def index(request):
    link = DromParser()
    return render(request, template_name='dromparser/index.html', context={'form':link})
