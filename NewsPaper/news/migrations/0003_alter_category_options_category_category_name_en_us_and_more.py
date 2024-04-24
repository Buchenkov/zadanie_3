# Generated by Django 5.0.1 on 2024-04-23 15:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_subscribers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_en_us',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_type_en_us',
            field=models.CharField(choices=[('NE', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_type_ru',
            field=models.CharField(choices=[('NE', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_en_us',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en_us',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(help_text='Имя категории', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category', verbose_name='Категории'),
        ),
    ]
