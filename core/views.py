from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from core.models import Room, Customer, Booking, Payment
from .forms import RoomForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Sum

@login_required
def dashboard(request):
    today = timezone.now().date()
    
    context = {
        'total_rooms': Room.objects.count(),
        'available_rooms': Room.objects.filter(is_available=True).count(),
        'total_customers': Customer.objects.count(),
        'total_bookings': Booking.objects.count(),
        'today_bookings': Booking.objects.filter(check_in=today).count(),
        'total_payments': Payment.objects.aggregate(total=Sum('amount'))['total'] or 0,
        'today_revenue': Payment.objects.filter(payment_date__date=today).aggregate(total=Sum('amount'))['total'] or 0,
    }
    
    return render(request, 'dashboard.html', context)



# ---------------------------------------------------------------------------------

@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room/room_list.html', {'rooms': rooms})


def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'room/room_form.html', {'form': form})

def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room/room_form.html', {'form': form})

@login_required
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'room/room_confirm_delete.html', {'room': room})




# ---------------------------------------------------------------------------------


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer/customer_list.html", {"customers": customers})


def customer_create(request):
    if request.method == "POST":
        Customer.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
        )
        return redirect("customer_list")

    return render(request, "customer/customer_form.html")


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.first_name = request.POST.get("first_name")
        customer.last_name = request.POST.get("last_name")
        customer.email = request.POST.get("email")
        customer.phone = request.POST.get("phone")
        customer.address = request.POST.get("address")
        customer.save()

        return redirect("customer_list")

    return render(request, "customer/customer_form.html", {"customer": customer})



def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect("customer_list")




# ---------------------------------------------------------------------------------


STATUS_CHOICES = ['Pending', 'Confirmed', 'CheckedIn', 'CheckedOut']

def booking_list(request):
    bookings = Booking.objects.select_related('customer', 'room').all().order_by('-check_in')
    return render(request, "booking/booking_list.html", {"bookings": bookings})

def booking_create(request):
    customers = Customer.objects.all()
    rooms = Room.objects.filter(is_available=True)

    if request.method == "POST":
        customer_id = request.POST.get("customer")
        room_id = request.POST.get("room")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        status = request.POST.get("status")

        customer = Customer.objects.get(id=customer_id)
        room = Room.objects.get(id=room_id)

        booking = Booking.objects.create(
            customer=customer,
            room=room,
            check_in=check_in,
            check_out=check_out,
            status=status
        )

        # Mark room unavailable
        room.is_available = False
        room.save()

        return redirect("booking_list")

    return render(request, "booking/booking_form.html", {
        "customers": customers,
        "rooms": rooms,
        "status_choices": STATUS_CHOICES
    })


def booking_edit(request, pk):
    booking = Booking.objects.get(id=pk)
    customers = Customer.objects.all()
    rooms = Room.objects.all()

    if request.method == "POST":
        booking.customer_id = request.POST.get("customer")
        booking.room_id = request.POST.get("room")
        booking.check_in = request.POST.get("check_in")
        booking.check_out = request.POST.get("check_out")
        booking.status = request.POST.get("status")
        booking.save()
        return redirect("booking_list")

    return render(request, "booking/booking_form.html", {
        "booking": booking,
        "customers": customers,
        "rooms": rooms,
        "status_choices": STATUS_CHOICES
    })

def booking_delete(request, pk):
    booking = Booking.objects.get(id=pk)
    # Optional: make room available again
    booking.room.is_available = True
    booking.room.save()
    booking.delete()
    return redirect("booking_list")


def booking_checkout(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    booking.status = "CheckedOut"
    booking.save()


    booking.room.is_available = True
    booking.room.save()
    return redirect('booking_list')



# ---------------------------------------------------------------------------------



def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payments/payment_list.html', {'payments': payments})


payment_methods = ['Cash', 'Card', 'Online']

def payment_create(request):
    bookings = Booking.objects.all()
    if request.method == 'POST':
        booking_id = request.POST.get('booking')
        amount = request.POST.get('amount')
        method = request.POST.get('method')
        payment_date = request.POST.get('payment_date') or timezone.now()

        booking = get_object_or_404(Booking, id=booking_id)
        Payment.objects.create(
            booking=booking,
            amount=amount,
            method=method,
            payment_date=payment_date
        )
        return redirect('payment_list')

    return render(request, 'payments/payment_form.html', {
        'bookings': bookings,
        'payment_methods': payment_methods
    })

def payment_edit(request, pk):
    payment = get_object_or_404(Payment, id=pk)
    bookings = Booking.objects.all()
    if request.method == 'POST':
        booking_id = request.POST.get('booking')
        amount = request.POST.get('amount')
        method = request.POST.get('method')
        payment_date = request.POST.get('payment_date') or timezone.now()

        booking = get_object_or_404(Booking, id=booking_id)
        payment.booking = booking
        payment.amount = amount
        payment.method = method
        payment.payment_date = payment_date
        payment.save()
        return redirect('payment_list')

    return render(request, 'payments/payment_form.html', {
        'payment': payment,
        'bookings': bookings,
        'payment_methods': payment_methods
    })



def payment_delete(request, pk):
    payment = Payment.objects.get(id=pk)
    payment.delete()
    return redirect('payment_list')



# ____________________________________________________________________________



def generate_invoice(request, pk):
    booking = Booking.objects.get(id=pk)
    template_path = 'booking/invoice.html'
    context = {'booking': booking}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="invoice_{booking.id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
