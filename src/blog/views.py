from django.shortcuts import render
from .models import Question, Post, Category


def questions_view(request, lang):
    return render(request, 'questions.html', {'questions':Question.objects.all(), 'lang': lang})

def index(request, lang):
    if lang == 'ru':
        return render(request, 'index_ru.html')
    return render(request, 'index_kg.html')

def answer_view(request, answer_id, lang):
    answer = Question.objects.get(id=answer_id)
    if lang == 'ru':
        return render(request, 'answer.html', {'answer':answer.answer_kg, 'lang':'ru'})
    return render(request, 'answer.html', {'answer':answer.answer_kg, 'lang':'ru'})

def post_view(request):
    posts = Post.objects.all()
    return render(request, 'post.html', context = {'posts':posts})

def category_view(request):
    categories = Category.objects.all()
    return render(request, 'category.html', context = {'categories':categories})
 
def post_details(request,post_id):
    posts = Post.objects.get(id=post_id)
    return render(request, 'post_details.html', context = {'posts':posts})


def category_details(request, cat_id):
    posts = Post.objects.filter(category__id = cat_id)
    
    return render(request, "post.html", context = {"posts":posts}) 
