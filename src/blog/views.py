from django.shortcuts import render
from .models import Question

# Create your views here.

def questions_view_ru(request):
    dummy = Question.objects.all()
    questions = []
    for i in dummy:
        questions.append({'id':i.id, 'question':i.question_ru, 'answer':i.answer_ru})
    return render(request, 'questions.html', {'questions':questions, 'lang':'ru'})

def answer_view_ru(request, answer_id):
    answer = Question.objects.get(id=answer_id)
    return render(request, 'answer.html', {'answer':answer.answer_ru, 'lang':'ru'})

def questions_view_kg(request):
    dummy = Question.objects.all()
    questions = []
    for i in dummy:
        questions.append({'id':i.id, 'question':i.question_kg, 'answer':i.answer_kg})
    return render(request, 'questions.html', {'questions':questions, 'lang':'kg'})

def answer_view_kg(request, answer_id):
    answer = Question.objects.get(id=answer_id)
    return render(request, 'answer.html', {'answer':answer.answer_kg, 'lang':'kg'})