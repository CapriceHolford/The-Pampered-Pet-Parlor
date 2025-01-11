from django.db import models 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Booking, PetProfile, UserProfile
from .forms import BookingForm, ContactForm, PetProfileForm, ChangeEmailForm, CustomPasswordChangeForm, EditProfileForm, ChangePhoneForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.dispatch import receiver 
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages
from django.db.models.signals import post_save

# Index view
def index(request):
    return render(request, 'pampered_pet_parlor/index.html')

# About page view
def about(request):
    return render(request, 'pampered_pet_parlor/about.html')

# Login page view
def login(request):
    return render(request, 'account/login.html')

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

def login_view(request):
    # Your login logic
    if user_logged_in:
        messages.success(request, "Welcome back!")
    return redirect('profile')

def logout_view(request):
    messages.success(request, "Goodbye!")
    return redirect('home')

@login_required
def book_appointment(request):
    # Fetch user's pet profile, if they have one
    pet_profile = PetProfile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.save()
            return redirect('index')  # Redirect to the success page (or wherever you'd like)
    else:
        # Prepopulate form with existing user data and pet profile (if available)
        initial_data = {
            'name': request.user.username,  # Prepopulate with user's username or other fields
            'email': request.user.email,    # Prepopulate email
        }
        
        # If there's a pet profile, prepopulate pet details (e.g., pet's name, breed)
        if pet_profile:
            initial_data.update({
                'pet_name': pet_profile.name,
                'pet_breed': pet_profile.breed,
                'pet_age': pet_profile.age,
            })
        
        form = BookingForm(initial=initial_data)
    
    return render(request, 'pampered_pet_parlor/book_appointment.html', {'form': form})

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

@login_required
def profile(request):
    # Get all bookings for the current user
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'account/profile.html', {'bookings': bookings})

@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            user = request.user
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profile')
    else:
        form = ChangeEmailForm(initial={'email': request.user.email})

    return render(request, 'account/change_email.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'account/change_password.html', {'form': form})

@login_required
def profile(request):
    # Check if the user has clicked "Edit Profile"
    edit_mode = request.GET.get('edit', False)
    
    if request.method == 'POST':
        # Handle form submissions for editing profile
        profile_form = EditProfileForm(request.POST, instance=request.user)
        phone_form = ChangePhoneForm(request.POST)

        if profile_form.is_valid() and phone_form.is_valid():
            profile_form.save()  # Save the updated profile data
            # Save phone number to the user's profile or a separate model if needed
            user_profile = request.user.userprofile
            user_profile.phone = phone_form.cleaned_data['phone']
            user_profile.save()
            return redirect('profile')  # Redirect to the same page after saving
    else:
        profile_form = EditProfileForm(instance=request.user)
        phone_form = ChangePhoneForm(initial={'phone': request.user.userprofile.phone})

    return render(request, 'account/profile.html', {
        'profile_form': profile_form,
        'phone_form': phone_form,
        'edit_mode': edit_mode,  # Pass edit_mode flag to the template
    })

@login_required
def add_pet_profile(request):
    if request.method == 'POST':
        form = PetProfileForm(request.POST)
        if form.is_valid():
            pet_profile = form.save(commit=False)
            pet_profile.user = request.user  # Ensure the pet is linked to the logged-in user
            pet_profile.save()
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = PetProfileForm()
    return render(request, 'account/add_pet_profile.html', {'form': form})

@login_required
def profile(request):
    # Fetch all pet profiles for the logged-in user (if they exist)
    pet_profiles = PetProfile.objects.filter(user=request.user)
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'account/profile.html', {
        'pet_profiles': pet_profiles,  # Passing the pet profiles here
        'bookings': bookings,
    })

@login_required
def edit_pet_profile(request, pet_id):
    pet_profile = get_object_or_404(PetProfile, id=pet_id, user=request.user)
    if request.method == 'POST':
        form = PetProfileForm(request.POST, request.FILES, instance=pet_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after saving the pet profile
    else:
        form = PetProfileForm(instance=pet_profile)

    return render(request, 'account/edit_pet_profile.html', {'form': form})

@login_required
def delete_pet_profile(request, pet_id):
    # Get the pet profile or return 404 if not found
    pet_profile = get_object_or_404(PetProfile, id=pet_id, user=request.user)

    # Delete the pet profile
    pet_profile.delete()

    # Redirect to the profile page after deletion
    return redirect('profile')

# delete and edit bookings
def delete_booking(request, booking_id):
    # Get the booking object or return a 404 if not found
    booking = get_object_or_404(Booking, id=booking_id)

    # Ensure that only the owner of the booking can delete it
    if booking.user == request.user:
        booking.delete()  # Delete the booking

    # Redirect to the profile page (or wherever you want after deletion)
    return redirect('profile')

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Ensure the user is the owner of the booking
    if booking.user != request.user:
        return redirect('profile')  # Or return an error message

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile after saving
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_appointment.html', {'form': form})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)  # Retrieve the blog post by its ID
    return render(request, 'account/blog_detail.html', {'post': post})


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Check if the user has a profile and create one if not
    if created:
        UserProfile.objects.get_or_create(user=instance)  # This ensures no duplicate profile
    else:
        instance.userprofile.save()

