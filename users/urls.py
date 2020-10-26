from django.urls import path

from .views import register_view, profile_view, profile_update_view


urlpatterns = [
    path('register/',  register_view, name='register'),
    path('account/profile', profile_view, name='profile'),
    path('account/update/profile', profile_update_view, name='update_profile'),
    ]
