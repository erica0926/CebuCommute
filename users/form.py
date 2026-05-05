from django import forms
from .models import User, Passenger, USER_TYPES, Driver
from transport.models import Jeepney, Route


class PassengerReg(forms.ModelForm):
    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "passenger"
        user.save()

        Passenger.objects.create(
            user=user,
            user_type=self.cleaned_data["user_type"]
        )

        return user


# firstname, lastname, username, password, email, usertype

class DriverReg(forms.ModelForm):
    route = forms.ModelChoiceField(queryset=Route.objects.all())
    max_capacity = forms.IntegerField(min_value=1, max_value=50)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "driver"
        user.save()

        route = self.cleaned_data["route"]
        capacity = self.cleaned_data["max_capacity"]

        jeep = Jeepney.objects.create(
            jeep_id=f"JEEP-{user.user_id}",
            route=route,
            max_capacity=capacity,
            current_passenger=0,
            status="avail"
        )
        
        Driver.objects.create(
            user=user,
            jeep=jeep
        )

        return user
