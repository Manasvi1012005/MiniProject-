from home.models import Booking
print("Total Amount for each booking:", [b.total_amount for b in Booking.objects.all()])
