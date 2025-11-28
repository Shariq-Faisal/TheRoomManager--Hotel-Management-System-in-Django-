from django.db import models
from django.utils import timezone

class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite')
    ]

    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.number} ({self.room_type})'


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'



    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('CheckedIn', 'Checked In'),
        ('CheckedOut', 'Checked Out'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    booked_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer.first_name} - Room {self.room.number}'



class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)           # 1 Payment per Booking  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    method = models.CharField(max_length=20, choices=[
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online'),
    ])

    def __str__(self):
        return f'Payment: {self.booking} - ${self.amount}'

