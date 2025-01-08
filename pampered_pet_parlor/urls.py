# urls.py
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact_view, name='contact'),  
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('booking/', views.booking, name='booking'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path ('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('edit-booking/<int:booking_id>/', views.edit_appointment, name='edit_appointment'),
    path('profile/', views.profile, name='profile'),
]

