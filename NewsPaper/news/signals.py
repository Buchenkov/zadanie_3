from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from news.models import PostCategory
from project import settings
from . tasks import send_email_task


# def send_notifications(preview, pk, title, subscribers):
#     """Отправка сообщений пользователю, сигнал вызывает эту Ф"""
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
#
# @receiver(m2m_changed, sender=PostCategory)   # делает Ф сигналом
# def notify_about_new_post(sender, instance, **kwargs):
#     # print(kwargs['action'], '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     """ Ф. сигнализирует о новой статье (когда добавляем категорию в статью и отправляем сообщение пользователям)"""
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers_emails = list(User.objects.filter(subscriptions__category__in=categories).values_list('email', flat=True))
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)


@receiver(m2m_changed, sender=PostCategory)   #
def notify_about_new_post(sender, instance, **kwargs):
    """ Ф. сигнализирует о новой статье (когда добавляем категорию в статью и отправляем сообщение пользователям)"""
    if kwargs['action'] == 'post_add':
        send_email_task.delay(instance.pk)

