from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField('도서명', max_length=100)
    publisher = models.CharField('출판사', max_length=100, blank=True)
    price = models.IntegerField('가격', blank=True, default=0)

    def __str__(self):
        return self.name

class Impression(models.Model):
    book = models.ForeignKey(Book, verbose_name='도서', 
                            related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('감상평', blank=True)

    def __str__(self):
        return self.comment