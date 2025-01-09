from django import forms
from .models import BlogPost
from .models import Booking
from .models import ContactMessage
from django.contrib.auth.forms import PasswordChangeForm
from .models import PetProfile, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')
        super().__init__(*args, **kwargs)
        if user:
            self.fields['pet'].queryset = PetProfile.objects.filter(user=user)

class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['name', 'breed', 'age', 'photo']

# Form to handle changing the email
class ChangeEmailForm(forms.Form):
    email = forms.EmailField(required=True)

# Form for changing the password
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Include the fields you want to allow users to edit
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ChangePhoneForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Now it's correctly imported
        fields = ('username', 'email', 'password1', 'password2')