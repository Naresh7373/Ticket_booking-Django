from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.urls import reverse
import logging
from .models import TrainBooking, BusBooking, FlightBooking
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def download_ticket_pdf(request, booking_type, booking_slug):
    if booking_type == "train":
        booking = TrainBooking.objects.get(slug=booking_slug)
    elif booking_type == "bus":
        booking = BusBooking.objects.get(slug=booking_slug)
    elif booking_type == "flight":
        booking = FlightBooking.objects.get(slug=booking_slug)
    else:
        return HttpResponse("Invalid booking type")

    # Create the HTTP response with PDF headers
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{booking_type}_ticket_{booking_slug}.pdf"'

    # Generate PDF
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 18)
    p.drawString(200, height - 100, f"{booking_type.title()} Ticket Confirmation")

    p.setFont("Helvetica", 12)
    p.drawString(100, height - 150, f"Passenger Name: {booking.passenger_name}")
    p.drawString(100, height - 170, f"From: {booking.from_place}")
    p.drawString(100, height - 190, f"To: {booking.to_place}")
    p.drawString(100, height - 210, f"Journey Date: {booking.journey_date}")
    p.drawString(100, height - 230, f"Seats: {booking.seats}")
    p.drawString(100, height - 250, f"Email: {booking.email}")
    p.drawString(100, height - 270, f"Phone: {booking.phone}")

    p.showPage()
    p.save()

    return response




# Create your views here.

def index(request):
    booking_title = "ticket booking"
    return render(request, 'ticket/index.html', {'booking_title': booking_title})

def train_booking(request):
    if request.method == "POST":
        booking = TrainBooking.objects.create(
            from_place=request.POST['from_place'],
            to_place=request.POST['to_place'],
            journey_date=request.POST['journey_date'],
            passenger_name=request.POST['passenger_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            seats=request.POST['seats'],
        )
        return redirect("bookingticket:booking_success", booking_type="train", booking_slug=booking.slug)

    return render(request, 'ticket/train_booking.html')

def bus_booking(request):
    if request.method == "POST":
        booking = BusBooking.objects.create(
            from_place=request.POST['from_place'],
            to_place=request.POST['to_place'],
            journey_date=request.POST['journey_date'],
            passenger_name=request.POST['passenger_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            seats=request.POST['seats'],
        )
        return redirect("bookingticket:booking_success", booking_type="bus", booking_slug=booking.slug)
    
    return render(request, 'ticket/bus_booking.html')

def flight_booking(request):
    if request.method == "POST":
        booking = FlightBooking.objects.create(
            from_place=request.POST['from_place'],
            to_place=request.POST['to_place'],
            journey_date=request.POST['journey_date'],
            passenger_name=request.POST['passenger_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            seats=request.POST['seats'],
        )
        return redirect("bookingticket:booking_success", booking_type="flight", booking_slug=booking.slug)
    
    return render(request, 'ticket/flight_booking.html')

def booking_success(request, booking_type, booking_slug):
    if booking_type == "train":
        booking = TrainBooking.objects.get(slug=booking_slug)
    elif booking_type == "bus":
        booking = BusBooking.objects.get(slug=booking_slug)
    elif booking_type == "flight":
        booking = FlightBooking.objects.get(slug=booking_slug)
    else:
        booking = None

    return render(request, 'ticket/booking_success.html', {
        "booking": booking,
        "booking_type": booking_type,
    })


# def detail(request, post_id):
#     # return HttpResponse(f"you are post detail page {post_id}")
#     return render(request, 'ticket/detail.html')
    # post = next((item for item in posts if item['id'] == post_id), None)
    # logger =logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    # return render(request,'ticket/detail.html', {'post': post})

def old_url_redirect(request):
    return redirect(reverse('bookingticket:new_page_url'))



def new_url_view(request):
    return HttpResponse("this is new url")


