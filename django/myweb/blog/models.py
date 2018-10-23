from django.db import models

# Create your models here.

class Post(models.Model): 
    title = models.CharField('TITLE',max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True,help_text = 'one word for title alias.')
    description = models.CharField('DESCRIPTION',max_length=100,blank=True, null=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date',auto_now_add =True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
