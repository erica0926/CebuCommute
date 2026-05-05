from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from decimal import Decimal

from .models import User, Passenger, Driver
from transport.models import Jeepney
from tickets.models import Ticket
from .form import PassengerReg, DriverReg


# Create your views here.
def passenger_register(request):
    if request.method == "POST":
        form = PassengerReg(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.role = "passenger"
            user.save()
            return redirect("passenger_login")
        else:
            print(form.errors)

    else:
        form = PassengerReg()

    return render(request, "passenger_register.html", {"form": form})


def passenger_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return render(request, "passenger_login.html",
                          {"error": "Invalid username or password"})

        request.session["user_id"] = user.user_id
        request.session["role"] = "passenger"

        if user.role == "passenger":
            return redirect("passenger_dashboard")

        elif user.role == "driver":
            return redirect("driver_login")

    return render(request, "passenger_login.html")


def passenger_dashboard(request):
    if request.session.get("role") != "passenger":
        return redirect("passenger_login.html")

    user = User.objects.get(user_id=request.session["user_id"])
    passenger = Passenger.objects.get(user=user)
    tickets = Ticket.objects.filter(passenger=passenger)

    return render(request, "passenger_dashboard.html", {
        "user": user, "user_type": passenger.get_user_type_display(), "tickets": tickets})


def driver_register(request):
    jeeps = Jeepney.objects.all()

    if request.method == "POST":
        form = DriverReg(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.role = "driver"
            user.save()

            return redirect("driver_login")

    else:
        form = DriverReg()

    return render(request, "driver_register.html", {"form": form})


def driver_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return render(request, "driver_login.html",
                          {"error": "Invalid username or password"})

        request.session["user_id"] = user.user_id
        request.session["role"] = "driver"

        if user.role == "driver":
            return redirect("driver_dashboard")

        elif user.role == "passenger":
            return redirect("passenger_login")

    return render(request, "driver_login.html")


def driver_dashboard(request):
    if request.session.get("role") != "driver":
        return redirect("driver_login")

    user = User.objects.get(user_id=request.session["user_id"])
    driver = Driver.objects.get(user=user)
    jeep = driver.jeep
    tickets = Ticket.objects.filter(jeep=jeep)

    print("LOGGED DRIVER:", user.username)
    print("DRIVER JEEP:", driver.jeep)
    print("TICKETS FOUND:", tickets.count())

    return render(request, "driver_dashboard.html", {
        "user": user,
        "tickets": tickets,
        "jeep": jeep
    })


def validate_ticket(request, ticket_id):
    if request.session.get("role") != "driver":
        return redirect("driver_login")

    user = User.objects.get(user_id=request.session["user_id"])
    driver = Driver.objects.get(user=user)

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if ticket.jeep != driver.jeep:
        return redirect("driver_dashboard")

    # update status
    if ticket.status == "active":
        ticket.status = "used"
    elif ticket.status == "used":
        ticket.status = "active"
    ticket.save()

    return redirect("driver_dashboard")
