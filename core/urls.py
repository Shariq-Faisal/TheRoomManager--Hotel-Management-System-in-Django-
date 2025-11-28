from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/add/', views.room_create, name='room_create'),
    path('rooms/<int:pk>/edit/', views.room_update, name='room_update'),
    path('rooms/<int:pk>/delete/', views.room_delete, name='room_delete'),

    path("customers/", views.customer_list, name="customer_list"),
    path("customers/edit/<int:pk>/", views.customer_edit, name="customer_edit"),
    path("customers/add/", views.customer_create, name="customer_create"),
    path("customers/delete/<int:pk>/", views.customer_delete, name="customer_delete"),

    path("bookings/", views.booking_list, name="booking_list"),
    path("bookings/add/", views.booking_create, name="booking_create"),
    path("bookings/edit/<int:pk>/", views.booking_edit, name="booking_edit"),
    path("bookings/delete/<int:pk>/", views.booking_delete, name="booking_delete"),
    path('bookings/checkout/<int:booking_id>/', views.booking_checkout, name='booking_checkout'),


    path('payments/', views.payment_list, name='payment_list'),
    path('payments/add/', views.payment_create, name='payment_create'),
    path('payments/edit/<int:pk>/', views.payment_edit, name='payment_edit'),
    path('payments/delete/<int:pk>/', views.payment_delete, name='payment_delete'),

    path('bookings/invoice/<int:pk>/', views.generate_invoice, name='booking_invoice'),

]
