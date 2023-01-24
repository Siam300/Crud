from django.shortcuts import redirect, render
from news.models import DailyNews

def INDEX(request):
    nws = DailyNews.objects.all()
    contex = {
        'nws':nws,
    }
    return render(request, 'index.html',contex)