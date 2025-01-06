# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact_view, name='contact'),  
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('booking/', views.booking, name='booking'),
]
