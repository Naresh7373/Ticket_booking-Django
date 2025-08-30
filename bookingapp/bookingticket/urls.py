from django.urls import path
from . import views

app_name = 'bookingticket'

urlpatterns = [
    path("", views.index, name="index"),
    path("train/", views.train_booking, name="train_booking"),
    path("bus/", views.bus_booking, name="bus_booking"),
    path("flight/", views.flight_booking, name="flight_booking"),
    path("success/<str:booking_type>/<slug:booking_slug>/", views.booking_success, name="booking_success"),
    # path(f"post/<int:post_id>", views.detail, name="detail"),
    path("new_something_url", views.new_url_view, name="new_page_url"),
    path("old_url", views.old_url_redirect, name="old_url"),
    path("download/<str:booking_type>/<slug:booking_slug>/", views.download_ticket_pdf, name="download_ticket"),


    
]
