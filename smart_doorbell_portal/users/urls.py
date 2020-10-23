from django.urls import path

from .views import register_view, profile_view


urlpatterns = [
    path('register/',  register_view, name='register'),
    path('account/profile', profile_view, name='profile'),
    path('recovery/', recover_password, name='forgot_pass'),
    ]
