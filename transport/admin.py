from django.contrib import admin
from .models import Route, Stop, RouteStop, Jeepney

# Register your models here.
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(RouteStop)
admin.site.register(Jeepney)
