# urls.py
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
    
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),  
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('booking/', views.booking, name='booking'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path ('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('edit-booking/<int:booking_id>/', views.edit_appointment, name='edit_appointment'),
    path('profile/', views.profile, name='profile'),
    path('profile/change-email/', views.change_email, name='change_email'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('profile/add-pet/', views.add_pet_profile, name='add_pet_profile'),
    path('profile/edit-pet/<int:pet_id>/', views.edit_pet_profile, name='edit_pet_profile'),
     path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('profile/delete-pet/<int:pet_id>/', views.delete_pet_profile, name='delete_pet_profile'),
    path('profile/book-appointment/', views.book_appointment, name='book_appointment'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)