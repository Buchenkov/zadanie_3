from django.urls import path

from . import views
from .views import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    # path('logout/', views.logout_view, name=''),  # account_logout - Администрирование Django
    # path('login/', views.login, name='account_login'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
]