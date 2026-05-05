"""
URL configuration for cebucommute project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import passenger_register, passenger_login, passenger_dashboard, driver_register, driver_login, \
    driver_dashboard, validate_ticket
from tickets.views import buy_ticket

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('registration/', passenger_register, name='passenger_register'),
    path('login/', passenger_login, name='passenger_login'),
    path('passenger/', passenger_dashboard, name='passenger_dashboard'),

    path('driver_registration/', driver_register, name='driver_register'),
    path('driver_login/', driver_login, name='driver_login'),
    path('driver_dashboard/', driver_dashboard, name='driver_dashboard'),

    path("buy-ticket/", buy_ticket, name="buy_ticket"),
    path("validate-ticket/<int:ticket_id>/", validate_ticket, name="validate_ticket"),
]
