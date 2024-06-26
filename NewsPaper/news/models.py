from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy    # импортируем «ленивый» геттекст с подсказкой

from datetime import datetime


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, help_text=_('category name'))  # связь с встроенной моделью пользователей User;
    ratingAuthor = models.SmallIntegerField(default=0)  # рейтинг пользователя

    def __str__(self):
        return self.user.username

    def update_rating(self):
        post_rating = self.posts.aggregate(pr=Coalesce(Sum('rating'), 0)).get('pr')
        comments_rating = self.user.comment.aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        posts_comments_rating = self.posts.aggregate(pcr=Coalesce(Sum('comment__rating'), 0))['pcr']

        self.ratingAuthor = post_rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)  # Категории новостей/статей
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='posts')  # связь «один ко многим» с моделью Author;
    NEWS = 'NE'  # поле с выбором — «статья» или «новость»;
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'))
    post_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    post_time = models.DateTimeField(auto_now_add=True)  # автоматически добавляемая дата и время создания;
    category = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категории')  # связь с моделью Category, PostCategory - промежуточная модель
    title = models.CharField(max_length=255)  # заголовок статьи/новости;
    text = models.TextField()  # текст статьи/новости;
    rating = models.IntegerField(default=0)  # рейтинг статьи/новости.
    verbose_name = pgettext_lazy('help text for MyModel model', 'This is the help text'),
    # slug = models.SlugField(max_length=128, unique=True)    # !

    def preview(self):  # возвращает начало статьи (предварительный просмотр)
        post_preview = f'{self.text[0:123]}...'
        return post_preview

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        # return '{}'.format(self.title)
        return f'{self.title}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу
        return reverse('post', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post;
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Category.


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь с моделью Post;
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')  # связь с моделью User
    text = models.TextField()  # текст комментария;
    comment_time = models.DateTimeField(auto_now_add=True)  # дата и время создания комментария;
    rating = models.IntegerField(default=0)  # рейтинг комментария.

    def __str__(self):
        return self.comment_post.author.user.username + '---' + str(self.id)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


