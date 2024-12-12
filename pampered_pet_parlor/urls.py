from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL of the app
    path('about/', views.about, name='about'),   #about page
    path('login/', views.login, name='login'),        # Login page
    path('register/', views.register, name='register'),  # Register page
    path('contact/', views.contact, name='contact'), # contact page
    path('faq/', views.faq, name='faq'),  # faq page
]