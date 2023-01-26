from django.shortcuts import render
from django.shortcuts import redirect, render
from news.models import DailyNews

def INDEX(request):
    nws = DailyNews.objects.all()
    contex = {
        'nws':nws,
    }
    return render(request, 'index.html',contex)

def ADD(request):
    if request.method ==  "POST":
        NewsTitle = request.POST.get('news_title')
        Details = request.POST.get('dtls')

        nws = DailyNews(
             newsTitle = NewsTitle,
             details = Details,
        )
        nws.save()
        return redirect('home')
    return render(request, 'index.html')

