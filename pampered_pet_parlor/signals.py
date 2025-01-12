from django.core.mail import send_mail
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from .models import UserProfile  # Ensure UserProfile is imported

# Send a welcome email when the user logs in
@receiver(user_logged_in)
def send_welcome_email(sender, request, user, **kwargs):
    send_mail(
        'Welcome Back!',
        'Thanks for logging in!',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )

# Create or update the UserProfile when the User object is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create the profile for the new user
        UserProfile.objects.create(user=instance)
    else:
        # Update the profile for existing users
        try:
            instance.profile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
