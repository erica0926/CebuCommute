from django.shortcuts import render, redirect

from .models import Ticket
from transport.models import Jeepney
from users.models import Passenger, User


# Create your views here.

def buy_ticket(request):
    if request.session.get("role") != "passenger":
        return redirect("")

    user = User.objects.get(user_id=request.session["user_id"])
    passenger = Passenger.objects.get(user=user)

    jeeps = Jeepney.objects.all()  # since you said 1 jeep for now

    if request.method == "POST":
        jeep_id = request.POST.get("jeep")

        if not jeep_id:
            return render(request, "buy_ticket.html", {
                "jeeps": jeeps,
                "error": "Please select a jeep"
            })

        jeep = Jeepney.objects.get(jeep_id=jeep_id)

        base_fare = 15
        discount = passenger.get_discount_rate()
        final_fare = base_fare * (1 - discount)

        Ticket.objects.create(
            passenger=passenger,
            jeep=jeep,
            fare=final_fare
        )

        return redirect("passenger_dashboard")

    return render(request, "buy_ticket.html", {"jeeps": jeeps})
