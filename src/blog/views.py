from django.shortcuts import render
from .models import Question


def questions_view(request):
    return render(request, 'questions.html', {'questions':Question.objects.all()})

def index(request, lang):
    if lang == 'ru':
        return render(request, 'index_ru.html')
    return render(request, 'index_kg.html')

def answer_view(request, answer_id, lang):
    answer = Question.objects.get(id=answer_id)
    if lang == 'ru':
        return render(request, 'answer.html', {'answer':answer.answer_kg, 'lang':'ru'})
    return render(request, 'answer.html', {'answer':answer.answer_kg, 'lang':'ru'})
