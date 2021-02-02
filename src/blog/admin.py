from django.contrib import admin
from django.contrib.admin import ModelAdmin
from trumbowyg.widgets import TrumbowygWidget
from .models import Post, Category
from django.forms import ModelForm
from modeltranslation.admin import TranslationAdmin


class PostAdminForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': TrumbowygWidget(),
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm




# @admin.register(Post)
# class PostModelAdmin(TranslationAdmin):
#     list_display = ("title", "body")


# @admin.register(Category)
# class CategoryAdmin(TranslationAdmin):
#     list_display = ("title")
    

admin.site.register(Category)

admin.site.register(Post, PostAdmin)


