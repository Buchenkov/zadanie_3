from django.contrib.auth.models import Group
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from news.views import NewsList
from .models import Subscription
from news.models import Category, Post


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('category_name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


@login_required     # ограничение по зарегистрированным пользователям
@csrf_protect   # автоматически проверяется CSRF-токен в получаемых формах
def subscribe(request, pk):
    user = request.user
    category = Category.objecrs.get(id=pk)
    category.subscribers.add(user)

    return redirect(f'news/categories/{category/pk}')

    # message = 'Вы успешно подписались на рассылку новостей категории'
    # return render(request, 'news/subscribe.html', {'category': category, 'message': message})


@login_required  # ограничение по зарегистрированным пользователям
@csrf_protect   # автоматически проверяется CSRF-токен в получаемых формах
def unsubscribe(request, pk):
    user = request.user
    category = Category.objecrs.get(id=pk)
    category.subscribers.add(user)

    return redirect(f'news/categories/{category / pk}')
