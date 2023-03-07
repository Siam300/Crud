from django.shortcuts import render
from django.shortcuts import redirect, render
from news.models import DailyNews
from .forms import NewsForm

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

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'index.html', {'form': form})

