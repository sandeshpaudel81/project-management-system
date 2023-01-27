from django.urls import path
from mgmtapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-signup/', views.user_signup, name='user_signup'),
]
