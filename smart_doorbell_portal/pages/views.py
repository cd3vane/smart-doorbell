from django.shortcuts import render

# Create your views here.
# list of mobile User Agents


def home_view(request):
    return render(request, 'pages/home.html')


def about_view(request):
    return render(request, 'pages/about.html', {})


def resume_view(request):
    return render(request, 'pages/resume_page.html', {})
