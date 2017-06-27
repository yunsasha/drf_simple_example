from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer
    )

from test_news.models import News


class NewsListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
        view_name='news-api:news-detail',
        lookup_field='pk'
    )

    class Meta:
        model = News
        fields = (
            'title',
            'text',
            'text2',
            'detail_url'
        )


class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = (
            'title',
            'text',
            'text2'
        )