from django.urls import path

from .views import event_log


urlpatterns = [
    path('log/', event_log, name='events'),
    ]
