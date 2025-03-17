from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('create/', views.create_blog, name='create_blog'),
    path('blogs/', views.blogs, name='blogs'),


    path('monetary_donations/', views.monetary_donations, name='monetary_donations'),
    path('features/', views.features, name='features'),
    path('team/', views.team, name='team'),

    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),

    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),



    path('view_pledged_books/', views.view_pledged_books, name='view_pledged_books'),
    # path('books_for_all/', views.books_for_all, name='books_for_all'),
    path('view_donated_books/', views.view_donated_books, name='view_donated_books'),

    path('donate-book/', views.donate_book, name='donate_book'),
    path('pledge-book/', views.pledge_book, name='pledge_book'),
    path('create-book-club/', views.create_book_club, name='create_book_club'),
    path('view-book-clubs/', views.view_book_clubs, name='view_book_clubs'),
    path('contact/', views.contact, name='contact'),
    path('messages/', views.view_messages, name='view_messages'),
    path('messages/read/<int:pk>/', views.read_message, name='read_message'),
    path('messages/delete/<int:pk>/', views.delete_message, name='delete_message'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('delete-testimonial/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),

    path('book-exchange/', views.book_exchange, name='book_exchange'),
    path('edit-impact/', views.edit_impact, name='edit_impact'),
    path('impact/', views.impact, name='impact'),


    path('book-appointment/', views.book_appointment, name='book_appointment'),

    path('book_exchange/', views.book_exchange, name='book_exchange'),

    path("upload-book/", views.upload_book, name="upload_book"),

    path('book-exchange/', views.book_exchange, name='book_exchange'),

    path('upload/', views.upload_book, name='upload_book'),
    path('book-exchange/', views.book_exchange, name='book_exchange'),
    path('mini-library/', views.mini_library, name='mini_library'),

    path('request-exchange/<int:book_id>/', views.request_exchange, name='request_exchange'),

    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book_list/', views.book_list, name='book_list'),
    path('download/<int:book_id>/', views.download_book, name='download_book'),
    path('request-exchange/<int:book_id>/', views.request_exchange, name='request_exchange'),



]

