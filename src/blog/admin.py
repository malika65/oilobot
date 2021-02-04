from django.contrib import admin
from django.contrib.admin import ModelAdmin
# from trumbowyg.widgets import TrumbowygWidget
from .models import Post, Category, Question


# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         widgets = {
#             'body_ru': TrumbowygWidget(),
#             'body_kg': TrumbowygWidget(),
#         }

# class PostAdmin(admin.ModelAdmin):
#     form = PostForm

 

admin.site.register(Category)

admin.site.register(Post)

admin.site.register(Question)
