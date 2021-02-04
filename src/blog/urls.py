from django.contrib import admin
from django.urls import path

from .views import questions_view, answer_view, index

urlpatterns = [
    path('<str:lang>', index),
    path('questions/', questions_view),
    path('answer/<int:answer_id>/<str:lang>', answer_view),
]