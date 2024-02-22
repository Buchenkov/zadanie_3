from django.urls import path
from django.views.generic import detail

# Импортируем созданные нами представления
from .views import *

urlpatterns = [
   path('news/', NewsList.as_view()),  # authors/
   path('news/<int:pk>/', PostView.as_view()),
   path('search/', Search.as_view(), name='search'),
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