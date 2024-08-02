from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request, 'core/about.html')

def index_view(request):
    return render(request, 'core/index.html')

def blog_view(request):
    return render(request, 'core/blog.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def services_view(request):
    return render(request, 'core/services.html')