from django.contrib import admin
from .models import *
from .views import Search

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(PostCategory)
# admin.site.register(Search)