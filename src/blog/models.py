from django.db import models

# Create your models here.

class Category(models.Model):
    title_ru = models.CharField(max_length=200,verbose_name = 'Заголовок на русском')
    title_kg = models.CharField(max_length=200,verbose_name = 'Заголовок на кыргызском')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    # def __str__(self):
    #     return self.title_ru

class Post(models.Model):
    title_ru = models.CharField(max_length=200,verbose_name = 'Заголовок на русском')
    title_kg = models.CharField(max_length=200,verbose_name = 'Заголовок на кыргызском')
    body_ru = models.TextField(max_length=1500, verbose_name = 'Тело поста на русском')
    body_kg = models.TextField(max_length=1500, verbose_name = 'Тело поста на кыргызском')
    img = models.ImageField(null=True,blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)



    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    # def __str__(self):
    #     return self.title_ru

class Question(models.Model):
    question_ru = models.CharField(max_length = 5, verbose_name='Вопрос')
    answer_ru = models.TextField(blank = True, verbose_name='Ответ')

    question_kg = models.CharField(max_length = 5, verbose_name='Суроо')
    answer_kg = models.TextField(blank = True, verbose_name='Жооп')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self):
        return self.question_ru
        