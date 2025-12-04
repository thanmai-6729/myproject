from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Home page view"""
    return render(request, 'college/index.html')

def about(request):
    """About page view"""
    return render(request, 'college/about.html')

def courses(request):
    """Courses page view"""
    return render(request, 'college/courses.html')

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you can add logic to save to database or send email
        # For now, we'll just render the page
        
    return render(request, 'college/contact.html')
