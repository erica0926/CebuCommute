from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("buy-ticket/", views.buy_ticket, name="buy_ticket"),
]
