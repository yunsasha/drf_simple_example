from django.shortcuts import render
from .serializers import NewsListSerializer, NewsDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from test_news.models import News
# Create your views here.


class NewsListApi(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetailApi(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class NewsUpdateApi(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer