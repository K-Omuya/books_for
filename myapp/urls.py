from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('blogs', views.blogs, name='blogs'),
    path('monetary_donations/', views.monetary_donations, name='monetary_donations'),
    path('features/', views.features, name='features'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),


    path('view_pledged_books/', views.view_pledged_books, name='view_pledged_books'),
    # path('books_for_all/', views.books_for_all, name='books_for_all'),
    path('view_donated_books/', views.view_donated_books, name='view_donated_books'),
    path('upload_book/', views.upload_book, name='upload_book'),

    path('donate-book/', views.donate_book, name='donate_book'),
    path('pledge-book/', views.pledge_book, name='pledge_book'),
    path('create-book-club/', views.create_book_club, name='create_book_club'),
    path('view-book-clubs/', views.view_book_clubs, name='view_book_clubs'),
    path('book-catalogue/', views.book_catalogue, name='book_catalogue'),
    path('contact/', views.contact, name='contact'),
    path('messages/', views.view_messages, name='view_messages'),
    path('messages/read/<int:pk>/', views.read_message, name='read_message'),
    path('messages/delete/<int:pk>/', views.delete_message, name='delete_message'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('delete-testimonial/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
    path('upload-book/', views.upload_book, name='upload_book'),
    path('book-exchange/', views.book_exchange, name='book_exchange'),
    path('edit-impact/', views.edit_impact, name='edit_impact'),
    path('impact/', views.impact, name='impact'),
]
