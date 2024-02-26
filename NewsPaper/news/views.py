from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .filters import NewsFilter
from .forms import PostForm
from .models import *


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-post_time'
    paginate_by = 10  # количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        # context['post_time'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class PostView(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — post_detail.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    # context_object_name = 'post'


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = '-post_time'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        if self.request.GET:
            return self.filterset.qs
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# @login_required
class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/post_create.html'

    # context_object_name = 'post_create'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news_create/':
            post.post.news = 'NE'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     if self.request.user != kwargs['instance'].user:
    #         return self.handle_no_permission()
    #     return kwargs


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'article/articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/articles_create/':
            post.post.news = 'AR'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('post')

    def get_success_url(self):
        return reverse_lazy('news')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('post')

    def get_success_url(self):
        return reverse_lazy('news')


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/post_create.html'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'article/articles_create.html'

