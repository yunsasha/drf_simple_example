from django.conf.urls import url
from .views import NewsListApi, NewsDetailApi, NewsUpdateApi

urlpatterns = [
    url(r'^news/$', NewsListApi.as_view(), name='news-list'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetailApi.as_view(), name='news-detail'),
    url(r'^news/edit/(?P<pk>\d+)/$', NewsUpdateApi.as_view(), name='news-update'),

]