from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Event
# Create your views here.

class EventLogView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/log_view1.html'
    context_object_name = 'events'
    ordering = ['-timestamp']
