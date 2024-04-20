"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),  # приложение flatpages
    path("accounts/", include("allauth.urls")),   # форма регистрации allauth
    path('', include('django.contrib.auth.urls')),
    path('', include('news.urls')),
    # path("accounts/", include("accounts.urls")),  # форма регистрации расширенная
    path('', include('accounts.urls')),
    path('', include('subscriptions.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
# http://127.0.0.1:8000/accounts/yandex/login/callback

# urlpatterns += i18n_patterns(path('', include('basic.urls')),)
