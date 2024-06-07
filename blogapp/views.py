
from django.shortcuts import render


def index(request):
    return render(request, 'blogapp/index.html')

def blogs(request):
    return render(request, 'blogapp/blogs.html')

def relative(request):
    return render(request,'blogapp/relative_url_templates.html')

def about(request):
    return render(request,'blogapp/about.html')
