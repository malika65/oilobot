from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Заголовок')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Заголовок')
    body = models.TextField(max_length=1500, verbose_name = 'Тело поста')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

class Question(models.Model):
    question = models.CharField(max_length = 5, verbose_name='Вопрос')
    answer = models.TextField(blank = True, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self):
        return self.question