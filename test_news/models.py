from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='News title')
    text = models.TextField(verbose_name='News text')
    text2 = models.TextField(verbose_name='News text2')

    def __str__(self):
        return self.title