from django.db import models
from decimal import Decimal

# Create your models here.
USER_TYPES = [
        ("UT-REG", "Regular"),
        ("UT-STD", "Student"),
        ("UT-SNR", "Senior"),
        ("UT-PWD", "PWD/Pregnant"),
    ]

DISCOUNT_MAP = {
    "UT-REG": 0.00,
    "UT-STD": 0.20,
    "UT-SNR": 0.20,
    "UT-PWD": 0.20,
}

class Passenger(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_discount_rate(self):
        return DISCOUNT_MAP.get(self.user_type, 0.00)


class Stop(models.Model):
    stop_id = models.CharField(max_length=50, primary_key=True)
    stop_name = models.CharField(max_length=50, unique=True)

    def __str__ (self):
        return self.stop_name


class Route(models.Model):
    route_id = models.CharField(max_length=50, primary_key=True)
    route_name = models.CharField(max_length=50)
    #origin = models.ForeignKey(Stop, on_delete=models.CASCADE)
    #destination = models.ForeignKey(Stop, on_delete=models.CASCADE)
    base_fare = models.DecimalField(max_digits=5, decimal_places=2, default=15.00)

    def __str__(self):
        return self.route_name


class RouteStop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    stop_order = models.PositiveIntegerField()

    def __str__ (self):
        return f"{self.route.route_id} {self.stop.stop_id} {self.stop_order}"


class Jeepney(models.Model):
    jeep_id = models.CharField(max_length=50, primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    max_capacity = models.IntegerField()
    current_passenger = models.PositiveIntegerField(default=0)
    status_types = [
        ("avail", "Available"),
        ("in_trans", "In Transit"),
        ("full", "Full"),
    ]
    status = models.CharField(max_length=20, choices=status_types, default="avail")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return f"{self.jeep_id} - {self.route.route_id}"


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    jeep = models.ForeignKey(Jeepney, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    fare = models.DecimalField(max_digits=5, decimal_places=2)
    final_fare = models.DecimalField(max_digits=5, decimal_places=2)
    discount_applied = models.DecimalField(max_digits=5, decimal_places=2)
    date_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        discount = Decimal(str(self.user.get_discount_rate()))

        self.fare = self.route.base_fare
        self.discount_applied = discount
        self.final_fare = self.route.base_fare * (Decimal(1.00) - discount)

        super().save(*args, **kwargs)

