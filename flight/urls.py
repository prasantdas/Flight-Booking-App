from django.urls import path
from .views import home, userLogin, userSignup, flightSearch, bookTicket, adminLogin, adminDashboard, addFlight, viewBookings, userLogout, adminLogout
from .views import bookForm, myBookings, cancelBooking
urlpatterns = [
    path('', home, name='home'),
    path('login/', userLogin, name='login'),
    path('signup/', userSignup, name='signup'),
    path('flight-search/', flightSearch, name='flightSearch'),
    path('book-ticket/<int:flight_number>/', bookTicket, name='bookTicket'),
    path('bookForm/<int:flight_number>/', bookForm, name='bookForm'),
    path('myadmin/login/', adminLogin, name='adminLogin'),
    path('myadmin/dashboard/', adminDashboard, name='adminDashboard'),
    path('myadmin/add-flight/', addFlight, name='addFlight'),
    path('myadmin/view-bookings/', viewBookings, name='viewBookings'),
    path('userLogout/', userLogout, name='userLogout'),
    path('adminLogout/', adminLogout, name='adminLogout'),
    path('my-bookings/', myBookings, name='myBookings'),
    path('cancel_booking/<int:booking_id>/', cancelBooking, name='cancel_booking'),
    # Add other URLs as needed
]
