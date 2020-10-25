from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def event_log(request):
    return render(request, 'events/log_view.html')
