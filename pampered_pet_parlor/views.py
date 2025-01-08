from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost, Booking
from .forms import BookingForm, ContactForm

# Index view
def index(request):
    return render(request, 'pampered_pet_parlor/index.html')

# About page view
def about(request):
    return render(request, 'pampered_pet_parlor/about.html')

# Login page view
def login(request):
    return render(request, 'pampered_pet_parlor/login.html')

# Register page view
def register(request):
    return render(request, 'pampered_pet_parlor/register.html')

# FAQ page view
def faq(request):
    return render(request, 'pampered_pet_parlor/faq.html')

# Blog page view
def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Fetch all blog posts, ordered by most recent
    return render(request, 'pampered_pet_parlor/blog.html', {'posts': posts})

# Booking view
def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        breed = request.POST.get('breed')
        size = request.POST.get('size')
        appointment_date = request.POST.get('date')
        appointment_time = request.POST.get('time')
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

# Contact view - handles form submission and displays a thank-you message
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            # Show a thank-you message on the same page
            return render(request, 'pampered_pet_parlor/contact.html', {'form': form, 'thank_you_message': 'Thank you for your message! We will get back to you soon.'})
    else:
        form = ContactForm()

    return render(request, 'pampered_pet_parlor/contact.html', {'form': form})

def book_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.save()
            return redirect('index')  # Redirect to a success page
    else:
        form = BookingForm()

    return render(request, 'book_appointment.html', {'form': form})

def edit_appointment(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)  # Ensure only users can edit their bookings
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after editing
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_appointment.html', {'form': form})

def profile(request):
    return render(request, 'pampered_pet_parlor/profile.html')  # Create a template for the profile page