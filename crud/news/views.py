from django.shortcuts import render

# Create your views here.
from news.models import DailyNews

def INDEX(request):
    nws = DailyNews.objects.all

    contex = {
        'nws':nws,
    }