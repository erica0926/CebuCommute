from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Passenger
from django.db import IntegrityError


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_user(request):
    error = None

    if request.method == 'POST':
        try:
            Passenger.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                email=request.POST.get('email'),
                user_type=int(request.POST.get('user_type'))
            )
            return redirect('index')

        except IntegrityError:
            error = "Username already exists. Please choose another one."

    return render(request, 'addUser.html', {'error': error})


def user_list(request):
    passengers = Passenger.objects.all()

    return render(request, 'userList.html', {'passengers': passengers})
