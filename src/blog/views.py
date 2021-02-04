from django.shortcuts import render
from .models import Post, Category
# Create your views here.
def index(request):
    return render(request, 'index.html')
   

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
