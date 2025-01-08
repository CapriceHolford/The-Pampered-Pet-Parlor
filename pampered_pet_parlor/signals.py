# signals.py
from django.core.mail import send_mail
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.conf import settings

@receiver(user_logged_in)
def send_welcome_email(sender, request, user, **kwargs):
    send_mail(
        'Welcome Back!',
        'Thanks for logging in!',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
