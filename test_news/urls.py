from django.conf.urls import url
from .views import NewsList

urlpatterns = [
    url(r'^', NewsList.as_view(), name='news-list'),
]