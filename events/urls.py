from django.urls import path

from .views import EventLogView


urlpatterns = [
    path('log/', EventLogView.as_view() , name='events'),
    ]
