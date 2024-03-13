import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('newspaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# * В первую очередь мы импортируем библиотеку для взаимодействия с операционной системой и саму библиотеку Celery.
# * Второй строчкой мы связываем настройки Django с настройками Celery через переменную окружения.
# * Далее мы создаем экземпляр приложения Celery и устанавливаем для него файл конфигурации. Мы также указываем
# пространство имен, чтобы Celery сам находил все необходимые настройки в общем конфигурационном файле settings.py.
# Он их будет искать по шаблону «CELERY_***».
# * Последней строчкой мы указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта.

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.signals.notify_about_new_post',
        'schedule': crontab(),  # hour=8, minute=0, day_of_week='monday'
        # 'args': ('agrs'),
    },
}