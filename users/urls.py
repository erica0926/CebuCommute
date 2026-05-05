from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('registration/', views.passenger_register, name='passenger_register'),
    path('login/', views.passenger_login, name='passenger_login'),
    path('passenger/', views.passenger_dashboard, name='passenger_dashboard'),

    path('driver_registration/', views.driver_register, name='driver_register'),
    path('driver_login/', views.driver_login, name='driver_login'),
    path('driver_dashboard/', views.driver_dashboard, name='driver_dashboard'),

    path("buy-ticket/", views.buy_ticket, name="buy_ticket"),
    path("validate-ticket/<int:ticket_id>/", views.validate_ticket, name="validate_ticket"),
]
