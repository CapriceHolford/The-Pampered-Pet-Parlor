from django import forms
from .models import BlogPost
from .models import Booking
from .models import ContactMessage

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']  # Exclude the `author` field
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'breed', 'size', 'date', 'time', 'service', 'notes']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'breed', 'size', 'date', 'time', 'service', 'notes']

