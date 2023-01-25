
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
        newsTitle = request.POST.get('news_title')
        details = request.POST.get('dtls')

        nws = DailyNews(
            newsTtitle = newsTitle,
            details = details
        )
        nws.save()
        return redirect('home')
    return render(request, 'index.html')