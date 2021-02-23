from .models import Product,Category,Comment
from django import forms


# cats = [('sports' , 'sports') , ('computers' , 'computers'),('clothes' , 'clothes')]
choices = Category.objects.all().values_list('title' , 'title')

cats = []

for item in choices:
    cats.append(item)

class AddProduct(forms.ModelForm):
    class  Meta:
        model = Product
        fields = ['name' , 'describtion' ,'price','category', 'image']

        widgets = {
            'category':forms.Select(choices=cats)
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_author' , 'comment_text']