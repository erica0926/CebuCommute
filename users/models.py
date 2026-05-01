from django.db import models

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
