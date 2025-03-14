from django.contrib import admin
from .models import CarMake, CarModel

# Tworzymy Inline do CarModel
class CarModelInline(admin.TabularInline):  # Możesz użyć StackedInline, jeśli chcesz bardziej rozbudowany widok
    model = CarModel
    extra = 1  # Liczba domyślnych formularzy, które będą dodane
    fields = ('name', 'car_type', 'year')  # Pola, które chcesz wyświetlić w formularzu CarModel

# Klasa admina dla CarMake
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Rejestrujemy CarModel jako Inline do CarMake
    list_display = ('name', 'description')  # Pola, które będą wyświetlane na liście

# Klasa admina dla CarModel (opcjonalna, jeśli chcesz dostosować widok CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'year')  # Pola do wyświetlenia
    search_fields = ('name', 'car_make__name')  # Możliwość wyszukiwania po nazwie modelu i marce

# Rejestrujemy modele w panelu admina
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
