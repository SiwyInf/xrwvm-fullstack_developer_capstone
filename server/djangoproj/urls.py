from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),  # Trasy Django app
    path('dealers/', TemplateView.as_view(template_name="index.html")),  # Jeśli masz osobną stronę dla dealerów
    path('', TemplateView.as_view(template_name="Home.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
