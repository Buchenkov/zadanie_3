from modeltranslation.translator import register, \
    TranslationOptions  # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться

from .models import Category, Post


# регистрируем наши модели для перевода

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'post_type',)
