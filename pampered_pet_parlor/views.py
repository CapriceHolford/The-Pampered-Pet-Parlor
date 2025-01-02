from django.shortcuts import render
from .models import BlogPost  # Import the BlogPost model for the blog view
from django.http import HttpResponse
from .models import Booking
from .forms import BookingForm

def index(request):
    return render(request, 'pampered_pet_parlor/index.html')  # Matches templates path

def about(request):
    return render(request, 'pampered_pet_parlor/about.html')

def login(request):
    return render(request, 'pampered_pet_parlor/login.html')

def register(request):
    return render(request, 'pampered_pet_parlor/register.html')

def contact(request):
    return render(request, 'pampered_pet_parlor/contact.html')

def faq(request):
    return render(request, 'pampered_pet_parlor/faq.html')

def blog(request):
    # Fetch all blog posts, ordered by the most recent first
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'pampered_pet_parlor/blog.html', {'posts': posts})

def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        breed = request.POST.get('breed')
        size = request.POST.get('size')
        appointment_date = request.POST.get('date')  # Match form field name
        appointment_time = request.POST.get('time')  # Match form field name
        service = request.POST.get('service')
        notes = request.POST.get('notes', '')

        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            breed=breed, 
            size=size, 
            date=appointment_date,
            time=appointment_time,
            service=service,
            notes=notes
        )
        return HttpResponse(f"Thank you, {name}! Your booking has been confirmed.")
    return render(request, 'pampered_pet_parlor/booking.html')