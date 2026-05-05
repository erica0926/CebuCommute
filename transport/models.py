from django.db import models


# Create your models here.

class Stop(models.Model):
    stop_id = models.CharField(max_length=50, primary_key=True)
    stop_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.stop_id} - {self.stop_name}"


class Route(models.Model):
    route_id = models.CharField(max_length=50, primary_key=True)
    route_name = models.CharField(max_length=50)
    # origin = models.ForeignKey(Stop, on_delete=models.CASCADE)
    # destination = models.ForeignKey(Stop, on_delete=models.CASCADE)
    base_fare = models.DecimalField(max_digits=5, decimal_places=2, default=15.00)

    def __str__(self):
        return self.route_name


class RouteStop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    stop_order = models.PositiveIntegerField()

    def __str__(self):
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

    def __str__(self):
        return f"{self.jeep_id} - {self.route.route_id}"
