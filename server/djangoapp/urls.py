from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Ścieżka dla logowania
    path('login/', views.login_user, name='login'),
    
    # Ścieżka dla wylogowywania
    path('logout/', views.logout_user, name='logout'),
    
    # Ścieżka dla rejestracji
    path('register/', views.registration, name='register'),
    
    # Ścieżka dla pobrania listy samochodów
    path('get_cars/', views.get_cars, name='getcars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
