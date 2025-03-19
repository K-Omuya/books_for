from django.contrib import admin
from .models import (
    Book, Pledge, BookClub, PledgedBook, BookDonation, Message,
    Testimonial, Impact, Appointment, Subscription, Blog, ExchangeTransaction, Profile
)

admin.site.register(Book)
admin.site.register(Pledge)
admin.site.register(BookClub)
admin.site.register(PledgedBook)
admin.site.register(BookDonation)
admin.site.register(Message)
admin.site.register(Testimonial)
admin.site.register(Impact)
admin.site.register(Appointment)
admin.site.register(Subscription)
admin.site.register(Blog)
admin.site.register(ExchangeTransaction)
admin.site.register(Profile)
