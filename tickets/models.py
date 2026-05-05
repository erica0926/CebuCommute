from django.db import models
from users.models import Passenger, Driver
from transport.models import Jeepney


# Create your models here.

class Ticket(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("used", "Used"),
        ("cancelled", "Cancelled"),
    ]

    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    jeep = models.ForeignKey(Jeepney, on_delete=models.CASCADE)

    fare = models.DecimalField(max_digits=6, decimal_places=2, default=15.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.passenger.user.username} - {self.status}"
