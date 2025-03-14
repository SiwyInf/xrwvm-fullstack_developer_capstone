# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Nazwa marki samochodu
    description = models.TextField(blank=True, null=True)  # Opis marki

    def __str__(self):
        return self.name  # Zwraca nazwę marki, aby była widoczna w panelu admina


# Create Car Model model
class CarModel(models.Model):
    SEDAN = 'SED'
    SUV = 'SUV'
    WAGON = 'WGN'
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Relacja wiele-do-jednego
    name = models.CharField(max_length=100)  # Nazwa modelu samochodu
    car_type = models.CharField(max_length=3, choices=CAR_TYPE_CHOICES)  # Typ samochodu
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]  # Rok produkcji samochodu
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Zwraca nazwę marki i modelu samochodu
