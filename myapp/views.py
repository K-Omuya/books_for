def home(request):
    return render(request, 'index.html')
def monetary_donations(request):
    return render(request, 'monetary_donations.html')

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def settings(request):
    return render(request, 'settings.html')

def features(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonials.html')



from .models import BookClub, BookDonation
from .forms import BookClubForm, BookDonationForm


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


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Appointment booked successfully!"})
        else:
            return JsonResponse({"success": False, "message": "Invalid data, please check your inputs."})
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Testimonial
from .forms import TestimonialForm

def testimonials_page(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save()

            # Render the updated testimonials section
            testimonials = Testimonial.objects.all().order_by('-id')
            testimonials_html = render_to_string('testimonials.html', {'testimonials': testimonials})

            return JsonResponse({"success": True, "testimonials_html": testimonials_html})

    testimonials = Testimonial.objects.all().order_by('-id')
    form = TestimonialForm()
    return render(request, 'testimonials.html', {'form': form, 'testimonials': testimonials})

from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

# Create Blog
@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('view_blogs')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

# View Blogs
def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs': blogs})

from django.shortcuts import render
from .models import PledgedBook

def view_pledged_books(request):
    pledged_books = PledgedBook.objects.all().order_by('-pledge_date')
    return render(request, 'view_pledged_books.html', {'pledged_books': pledged_books})
from django.shortcuts import render, redirect
from .forms import PledgedBookForm
from .models import PledgedBook

def pledge_book(request):
    if request.method == "POST":
        form = PledgedBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_pledged_books')  # Redirect to the pledged books list
    else:
        form = PledgedBookForm()

    return render(request, 'pledge_book.html', {'form': form})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Upload a book
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_exchange')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})

# Display book exchange library
def book_exchange(request):
    books = Book.objects.all()
    return render(request, 'book_exchange.html', {'books': books})

@login_required
def mini_library(request):
    user_books = Book.objects.filter(donor=request.user)
    return render(request, 'mini_library.html', {'books': user_books})
@login_required
def view_requests(request):
    exchange_requests = ExchangeRequest.objects.filter(book__donor_name=request.user.username)
    return render(request, 'view_requests.html', {'exchange_requests': exchange_requests})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, ExchangeRequest

from django.shortcuts import render
from .models import Book

def book_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort_by', '')

    books = Book.objects.all()
    if search_query:
        books = books.filter(title__icontains=search_query)

    if sort_by:
        books = books.order_by(sort_by)

    return render(request, 'book_exchange.html', {'books': books})

from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


@login_required
def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.download_available and book.document:
        return render(request, 'download.html', {'book': book})
    return render(request, 'error.html', {'message': 'This book cannot be downloaded.'})

@login_required
def request_exchange(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        ExchangeRequest.objects.create(book=book, requester=request.user)
        return redirect('book_list')  # Redirect back to the book list
    return render(request, 'request_exchange.html', {'book': book})
