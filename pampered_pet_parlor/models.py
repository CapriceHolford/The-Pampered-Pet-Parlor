from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Link to User model

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    breed = models.CharField(max_length=100, blank=True, null=True)  
    size = models.CharField(max_length=50, blank=True, null=True) 
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.service} on {self.date} at {self.time}"

def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        appointment_date = request.POST.get('appointment_date')  # Requires a date field in your form
        message = request.POST.get('message', '')
        Booking.objects.create(name=name, email=email, appointment_date=appointment_date, message=message)
        return HttpResponse(f"Thank you, {name}! Your booking has been confirmed.")
    return render(request, 'pampered_pet_parlor/booking.html')