from django.db import models
from decimal import Decimal

# Create your models here.
USER_ROLES = [
    ("passenger", "Passenger"),
    ("driver", "Driver"),
]

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


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    role = models.CharField(max_length=20, choices=USER_ROLES)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jeep = models.ForeignKey("transport.Jeepney", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - jeep owned: {self.jeep.jeep_id}"


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user_type}"

    def get_discount_rate(self):
        return DISCOUNT_MAP.get(self.user_type, 0.00)
