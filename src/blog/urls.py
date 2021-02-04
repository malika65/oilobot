from django.contrib import admin
from django.urls import path

from .views import questions_view_ru, answer_view_ru, questions_view_kg, answer_view_kg

urlpatterns = [
    path('questions-ru', questions_view_ru),
    path('answer-ru/<int:answer_id>', answer_view_ru),
    path('questions-kg', questions_view_kg),
    path('answer-kg/<int:answer_id>', answer_view_kg),
]