from django.contrib import admin
from django.urls import path,include
from .views import index,post_view,category_view,post_details,category_details


app_name = 'posts'


urlpatterns = [
    path('',index),
    path('post/',post_view,name='post'),
    path('category/',category_view,name='category'),
    path('post_details/<int:post_id>/',post_details,name='post_details'),
    path('category/<int:cat_id>/', category_details, name = 'cat_details'),



    

]