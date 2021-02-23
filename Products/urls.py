from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('detail/<int:id>', detail  , name = 'detail'),
    path('delete/<int:id>', delete  , name = 'delete'),
    path('update/<int:pk>', update.as_view()  , name = 'update'),
    path('dashboard', dashboard  , name = 'dashboard'),
    path('addcategory/' , AddCategoryView.as_view() , name = 'addcategory'),
    path('category/<str:cats>' , CategoryView , name = 'categoryview'),
    path('comment/<int:id>', comment , name = 'comment'),
]