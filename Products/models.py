from django.db import models

from django.shortcuts import reverse

from djchoices import ChoiceItem, DjangoChoices
# Create your models here.

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("index")
    
    

class Product(models.Model):
    user =  models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    name = models.CharField(max_length=50 , verbose_name='Product Name')
    describtion = RichTextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True , null = True)
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length = 50 , default = 'coding')

    def __str__(self):
        return self.name

    def get_absolute_url(self): # new
        return reverse('dashboard')   


class Comment(models.Model):
    product = models.ForeignKey(Product , on_delete = models.CASCADE , related_name='comments')
    comment_author = models.CharField(max_length=20)
    comment_text = models.CharField(max_length=140)

    

    

