from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register_view, profile_view, profile_update_view


urlpatterns = [
    path('register/',  register_view, name='register'),
    path('account/profile', profile_view, name='profile'),
    path('account/update-profile', profile_update_view, name='update_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    ]
