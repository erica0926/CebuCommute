from django.contrib import admin
from .models import User, Driver, Passenger

# Register your models here.
admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Passenger)
