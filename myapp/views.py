def home(request):
    return render(request, 'index.html')
def monetary_donations(request):
    return render(request, 'monetary_donations.html')

def index(request):
    return render(request, 'index.html')
def edit_profile(request):
    return render(request, 'edit_profile.html')
def about(request):
    return render(request, 'about.html')
from django.contrib.auth.decorators import login_required

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


from django.shortcuts import render, redirect
from .models import Book
from .forms import BookUploadForm
from django.shortcuts import render, redirect
from .forms import BookUploadForm
from .models import Book

def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_exchange')  # Redirect to a page displaying the uploaded books
    else:
        form = BookUploadForm()
    return render(request, 'upload_book.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.db.models import Q

# Display books
def book_exchange(request):
    books = Book.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(genre__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    return render(request, 'book_exchange.html', {'books': books, 'search_query': search_query})


def pay_for_book(request, book_id, action):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        phone = request.POST.get('phone')

        # Redirect to STK push view with book details
        return redirect('stk', book_id=book.id, action=action, phone=phone)

    return render(request, 'pay.html', {'book_id': book.id, 'action': action, 'book': book})

from django.shortcuts import get_object_or_404, redirect, render
from django.http import FileResponse, HttpResponse
from django.db import transaction
from .models import Book, ExchangeTransaction  # Ensure you have this model
import os

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.db import transaction
from .models import Book, ExchangeTransaction

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import transaction
from .models import Book, ExchangeTransaction


def stk_push(request, book_id, action):
    if request.method == "POST":
        phone = request.POST.get('phone')

        if not phone:
            return HttpResponse("Phone number is required.", status=400)

        book = get_object_or_404(Book, id=book_id)

        # Simulate M-Pesa STK push
        payment_successful = True

        if payment_successful:
            with transaction.atomic():
                transaction_obj = ExchangeTransaction.objects.create(
                    user=request.user,
                    book=book,
                    action=action,
                    payment_status="Paid",
                    status="Completed" if action == "download" else "In Progress"
                )

                # If action is download, assign file link
                if action == "download":
                    transaction_obj.download_link = book.document
                    transaction_obj.save()

            return redirect('mini_library')  # Redirect after payment

        return HttpResponse("Payment failed. Please try again.", status=400)

    return HttpResponse("Invalid request method.", status=405)


from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse
import os

def download(request, book_id, action):
    book = get_object_or_404(Book, id=book_id)

    if action == "download":
        if book.document:  # Assuming `document` is a FileField in your model
            file_path = book.document.path
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
            else:
                return HttpResponse("File not found", status=404)
        else:
            return HttpResponse("No document available for this book", status=404)

    return HttpResponse("Invalid action", status=400)



def mini_library(request):
    transactions = ExchangeTransaction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'mini_library.html', {'transactions': transactions})
def pay(request, book_id, action):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'pay.html', {'book_id': book.id, 'action': action})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileUpdateForm, UserUpdateForm

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import ExchangeTransaction

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("profile")

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in after password change
            messages.success(request, "Your password has been updated successfully!")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        password_form = PasswordChangeForm(request.user)

    # Retrieve transactions
    transactions = ExchangeTransaction.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "password_form": password_form,
        "transactions": transactions,  # Pass transactions to the template
    })

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def auth(request):
    if request.method == "POST":
        if "login" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                messages.error(request, "Invalid username or password.")

        elif "register" in request.POST:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if password1 != password2:
                messages.error(request, "Passwords do not match!")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Registration successful! You can now log in.")

    return render(request, "auth.html")
