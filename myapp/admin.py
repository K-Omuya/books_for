
from django.contrib import admin
from .models import Impact, BookClub, BookDonation,Book,Blog,PledgedBook,Testimonial,Message,Pledge,FeaturedBook

admin.site.register(Impact)
admin.site.register(BookClub)
admin.site.register(BookDonation)
admin.site.register(Book)
admin.site.register(Blog)
admin.site.register(FeaturedBook)
admin.site.register(PledgedBook)
admin.site.register(Testimonial)
admin.site.register(Message)
admin.site.register(Pledge)


