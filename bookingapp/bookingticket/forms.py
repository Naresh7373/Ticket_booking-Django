from django import forms
from .models import BusBooking, TrainBooking, FlightBooking

class BusBookingForm(forms.ModelForm):
    class Meta:
        model = BusBooking
        fields = ['passenger_name', 'from_place', 'to_place', 'journey_date', 'seats', 'email', 'phone']

class TrainBookingForm(forms.ModelForm):
    class Meta:
        model = TrainBooking
        fields = ['passenger_name', 'from_place', 'to_place', 'journey_date', 'seats', 'email', 'phone']

class FlightBookingForm(forms.ModelForm):
    class Meta:
        model = FlightBooking
        fields = ['passenger_name', 'from_place', 'to_place', 'journey_date', 'seats', 'email', 'phone']
