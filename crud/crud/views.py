from django.shortcuts import redirect, render

def INDEX(request):
    return render(request, 'index.html')