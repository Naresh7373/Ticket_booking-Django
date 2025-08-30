from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.

class BusBooking(models.Model):
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    journey_date = models.DateField()
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    seats = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.passenger_name}-{self.from_place}-{self.to_place}")
            unique_id = str(uuid.uuid4())[:8]
            self.slug = f"{base_slug}-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket #{self.id} | {self.passenger_name} - {self.from_place} to {self.to_place}"
    

class TrainBooking(models.Model):
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    journey_date = models.DateField()
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    seats = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.passenger_name}-{self.from_place}-{self.to_place}")
            unique_id = str(uuid.uuid4())[:8]
            self.slug = f"{base_slug}-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket #{self.id} | {self.passenger_name} - {self.from_place} to {self.to_place}"

    
class FlightBooking(models.Model):
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    journey_date = models.DateField()
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    seats = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.passenger_name}-{self.from_place}-{self.to_place}")
            unique_id = str(uuid.uuid4())[:8]
            self.slug = f"{base_slug}-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket #{self.id} | {self.passenger_name} - {self.from_place} to {self.to_place}"




# from django.db import models

# class BaseBooking(models.Model):
#     from_place = models.CharField(max_length=100)
#     to_place = models.CharField(max_length=100)
#     journey_date = models.DateField()
#     passenger_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     seats = models.PositiveIntegerField()

#     class Meta:
#         abstract = True  # This won’t create a table in DB

#     def __str__(self):
#         return f"{self.passenger_name} - {self.from_place} to {self.to_place}"

# class BusBooking(BaseBooking):
#     pass

# class TrainBooking(BaseBooking):
#     pass

# class FlightBooking(BaseBooking):
#     pass

    


