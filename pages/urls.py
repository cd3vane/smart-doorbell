from django.urls import path

from pages.views import home_view, resume_view,  about_view


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('home/', home_view, name='home'),
    path('resume/', resume_view, name='resume'),
    ]
