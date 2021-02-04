from django.contrib import admin
from .views import questions_view, answer_view, index, post_view,category_view,post_details,category_details
from django.urls import path

urlpatterns = [
    path('<str:lang>', index),
    path('questions/<str:lang>', questions_view),
    path('answer/<int:answer_id>/<str:lang>', answer_view),
    path('post/',post_view,name='post'),
    path('category/',category_view,name='category'),
    path('post_details/<int:post_id>/',post_details,name='post_details'),
    path('category/<int:cat_id>/', category_details, name = 'cat_details'),
]