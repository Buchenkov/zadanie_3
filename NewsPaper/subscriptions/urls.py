from django.urls import path

# Импортируем созданные нами представления
from .views import *
from .views import (subscriptions)

urlpatterns = [
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]