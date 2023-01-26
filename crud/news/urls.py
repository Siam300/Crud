from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news.views import INDEX, ADD, news_create

urlpatterns = [
    path('',INDEX,name='home'),
    # path('add',ADD,name='add'),
    path('add', news_create, name='news_create'),
] 