from django.urls import path
from django.views.generic import detail
from django.views.decorators.cache import cache_page
from accounts import views
from .tasks import weekly_send_email_task
# Импортируем созданные нами представления
from .views import *

urlpatterns = [
   path('', NewsList.as_view()),
   path('news/', NewsList.as_view(), name='news'),
   path('news/<int:pk>/', PostView.as_view(), name='post'),  # ,...cache_page(300)(PostView.as_view()), name='post'),
   path('search/', Search.as_view(), name='search'),
   path('news/post_create/', PostCreate.as_view(), name='post_create'),
   path('article/articles_create/', ArticleCreate.as_view(), name='articles_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/<int:pk>/edit', ArticleUpdate.as_view(), name='articles_edit'),
   path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
   path('upgrade/', upgrade_me, name='upgrade'),
   # path('news/post_detail/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),  # страница категории и подписка
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),  # подписка на категорию (успешно подписался)
   path('', weekly_send_email_task, name='weekly_send_email_task'),   # еженедельная подписка через tasks и celery
]

# urlpatterns = [
#    path('', NewsList.as_view()),
#    path('post/<int:pk>/', Post.as_view())
#    # path — означает путь.
#    # В данном случае путь ко всем товарам у нас останется пустым.
#    # Т.к. наше объявленное представление является классом,
#    # а Django ожидает функцию, нам надо представить этот класс в виде view.
#    # Для этого вызываем метод as_view.
#    # path('', NewsList.as_view()),
#    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
#    # int — указывает на то, что принимаются только целочисленные значения
#    # path('', PostDetail.as_view()),
#
#    # path('new/<str:slug>', detail)
# ]