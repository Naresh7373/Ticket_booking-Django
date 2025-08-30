from django.contrib import admin
from .models import TrainBooking, BusBooking, FlightBooking

# Register your models here.

from django.contrib import admin
from .models import TrainBooking, BusBooking, FlightBooking


@admin.register(TrainBooking)
class TrainBookingAdmin(admin.ModelAdmin):
    list_display = ("passenger_name", "from_place", "to_place", "journey_date", "seats", "email", "phone", "slug")
    search_fields = ("passenger_name", "email", "phone") 
    list_filter = ("journey_date", "from_place", "to_place")


@admin.register(BusBooking)
class BusBookingAdmin(admin.ModelAdmin):
    list_display = ("passenger_name", "from_place", "to_place", "journey_date", "seats", "email", "phone", "slug")
    search_fields = ("passenger_name", "email", "phone")
    list_filter = ("journey_date", "from_place", "to_place")


@admin.register(FlightBooking)
class FlightBookingAdmin(admin.ModelAdmin):
    list_display = ("passenger_name", "from_place", "to_place", "journey_date", "seats", "email", "phone", "slug")
    search_fields = ("passenger_name", "email", "phone")
    list_filter = ("journey_date", "from_place", "to_place")
