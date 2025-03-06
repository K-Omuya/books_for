from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def blogs(request):
    return render(request, 'blog.html')

def features(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def monetary_donations(request):
    return render(request, 'monetary_donations.html')
def testimonial(request):
    return render(request, 'testimonials.html')

def contact(request):
    return render(request, 'contact.html')
from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'blogs': blogs})


def donate_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_catalogue')
    else:
        form = BookForm()
    return render(request, 'donate_book.html', {'form': form})

def upload_book(request):
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PledgeForm()
    return render(request, 'upload_book.html', {'form': form})


from .models import BookClub
from .forms import BookClubForm


def view_book_clubs(request):
    clubs_by_county = {}
    for club in BookClub.objects.all():
        if club.county not in clubs_by_county:
            clubs_by_county[club.county] = []
        clubs_by_county[club.county].append(club)

    return render(request, 'view_book_clubs.html', {'clubs_by_county': clubs_by_county})


def create_book_club(request):
    if request.method == 'POST':
        form = BookClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_book_clubs')
    else:
        form = BookClubForm()
    return render(request, 'create_book_club.html', {'form': form})





def book_catalogue(request):
    books = Book.objects.all()
    return render(request, 'book_exchange_catalogue.html', {'books': books})




from django.shortcuts import render, redirect
from .models import PledgedBook
from .forms import PledgedBookForm

def pledge_book(request):
    if request.method == 'POST':
        form = PledgedBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_pledged_books')  # Redirect to pledged books list
    else:
        form = PledgedBookForm()
    return render(request, 'pledge_book.html', {'form': form})

def view_pledged_books(request):
    pledged_books = PledgedBook.objects.all().order_by('-pledge_date')  # Latest pledges first
    return render(request, 'view_pledged_books.html', {'pledged_books': pledged_books})

from .models import BookDonation
from .forms import BookDonationForm

def donate_book(request):
    if request.method == 'POST':
        form = BookDonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_donated_books')
    else:
        form = BookDonationForm()
    return render(request, 'donate_book.html', {'form': form})

def view_donated_books(request):
    books = BookDonation.objects.all().order_by('-donated_at')
    return render(request, 'view_donated_books.html', {'books': books})


from django.shortcuts import render, redirect
from django.contrib import messages


from django.http import HttpResponse


from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm

# Contact form submission
def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            return redirect('view_messages')  # Redirect after saving
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})

# View all messages
def view_messages(request):
    messages = Message.objects.all().order_by('-created_at')  # Latest messages first
    return render(request, 'view_messages.html', {'messages': messages})

# Read a single message
def read_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'read_message.html', {'message': message})

# Delete a message
def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('view_messages')
    return render(request, 'delete_message.html', {'message': message})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Testimonial
from .forms import TestimonialForm


# Display testimonials and handle form submission
def testimonials(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonials')  # Refresh page to show new testimonial

    return render(request, 'testimonials.html', {'testimonials': testimonials, 'form': form})


# Delete testimonial (admin view)
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonials')  # Redirect to testimonials page
    return render(request, 'delete_testimonial.html', {'testimonial': testimonial})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # Payment verification logic can be added here before saving the book
            form.save()
            return redirect('book_exchange')  # Redirect to book exchange page
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})

def book_exchange(request):
    books = Book.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        books = books.filter(title__icontains=query)  # Allow search by title
    return render(request, 'book_exchange.html', {'books': books})


from django.shortcuts import render
from .models import Impact

def impact(request):
    impact = Impact.objects.first()  # Assuming there's only one Impact entry
    return render(request, 'impact.html', {'impact': impact})

from django.shortcuts import render, redirect
from .forms import ImpactForm

def edit_impact(request):
    impact = Impact.objects.first()
    if request.method == 'POST':
        form = ImpactForm(request.POST, instance=impact)
        if form.is_valid():
            form.save()
            return redirect('impact_view')
    else:
        form = ImpactForm(instance=impact)
    return render(request, 'edit_impact.html', {'form': form})
