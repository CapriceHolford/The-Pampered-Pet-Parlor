from django.shortcuts import render

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