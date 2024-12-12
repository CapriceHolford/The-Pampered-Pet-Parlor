from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pampered_pet_parlor.urls')),
    path('admin/', admin.site.urls),
]