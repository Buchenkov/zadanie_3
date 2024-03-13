import datetime
import time

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news.models import Post, PostCategory, Category
from project import settings
from project.celery import app


# @app.task
# def text():
#     time.sleep(10)
#     # print('Hello!!')
#     return 'hello world!'


@app.task
def send_email_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    title = post.category
    subscribers = []
    for category in categories:
        subscribers_users = category.subscribers.all()
        for sub_user in subscribers_users:
            subscribers.append(sub_user.email)
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': f'{post.title}',
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()


@app.task
def weekly_send_email_task(pk):  # Запуск из celery
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(post_time__gte=last_week)
    categories = set(posts.values_list('category__category_name', flat=True))
    subscribers = set(Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()