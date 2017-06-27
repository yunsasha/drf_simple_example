from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView

from .models import News
# Create your views here.


class NewsList(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'