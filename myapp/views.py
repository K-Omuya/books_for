
from requests.auth import HTTPBasicAuth
import requests
from django.http import HttpResponse


from myapp.credentials import MpesaAccessToken, LipanaMpesaPpassword

def home(request):
    return render(request, 'index.html')

def blogs(request):
    return render(request, 'blog.html')
def upload_fee(request):
    return render(request, 'upload_fee.html')

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
from django.shortcuts import render, redirect
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

def monetary_donations(request):
    return render(request, 'monetary_donations.html')
def testimonial(request):
    return render(request, 'testimonials.html')

def contact(request):
    return render(request, 'contact.html')
from django.shortcuts import render
from .models import Blog

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
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


# views.py
from django.http import JsonResponse
from django.shortcuts import render
from .forms import SubscriptionForm

def subscribe(request):
    if request.method == 'POST' and request.is_ajax():
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Subscribed successfully!'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid email!'}, status=400)
    return JsonResponse({'error': 'Invalid request!'}, status=400)

def subscription_page(request):
    form = SubscriptionForm()
    return render(request, 'subscription.html', {'form': form})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .mpesa import initiate_payment
from .models import Payment

@csrf_exempt
def start_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        phone = data.get("phone_number")
        response = initiate_payment(phone)

        # Save payment request
        Payment.objects.create(phone_number=phone, transaction_id=response.get("CheckoutRequestID"), status="Pending")

        return JsonResponse({"success": True, "message": "Payment initiated. Approve it on your phone."})


def check_payment_status(request):
    phone = request.GET.get("phone")
    payment = Payment.objects.filter(phone_number=phone, status="Completed").first()

    if payment:
        return JsonResponse({"paid": True})
    return JsonResponse({"paid": False})

from django.shortcuts import render, redirect
from .forms import BookForm

def upload_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_exchange")
    else:
        form = BookForm()
    return render(request, "upload_book.html", {"form": form})



from django.shortcuts import render
from .models import Book

def book_exchange(request):
    """
    Handles the book exchange view with support for searching and sorting books.
    """
    # Retrieve query parameters
    search_query = request.GET.get('q', '')  # The search query for book titles
    sort_by = request.GET.get('sort_by', 'title')  # The sorting criteria, default to 'title'

    # Filter books based on the search query
    if search_query:
        books = Book.objects.filter(title__icontains=search_query)
    else:
        books = Book.objects.all()

    # Sort books based on the selected criteria
    if sort_by in ['title', 'author', 'genre']:
        books = books.order_by(sort_by)

    # Pass context to the template
    context = {
        'books': books,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'book_exchange.html', context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json





def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')


from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import base64


def stk(request):
    if request.method == "POST":
        phone = request.POST.get('phone')

        # Validate Phone Number
        if not phone or len(phone) != 12 or not phone.startswith('254'):
            return JsonResponse({"error": "Invalid phone number. Ensure it starts with 254 and is 12 digits long."},
                                status=400)

        # Set Amount to Ksh. 200
        amount = 200

        # Get Access Token
        consumer_key = 'rmNIDA9T8cvKiNARUzpWq6IGO7nAaPGVXQMXkIKRlUZ1g3lt'
        consumer_secret = 'R1SBVyJaTEt0GljTaA6aVR77fjZNfzARnKrU5k2Tu8q6Wxdj1FoS7AEGaajq3Zh7'
        access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        r = requests.get(access_token_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        access_token = json.loads(r.text).get('access_token')

        # STK Push Configuration
        lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
        business_shortcode = "174379"
        passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

        # Encode the password
        data_to_encode = business_shortcode + passkey + lipa_time
        online_password = base64.b64encode(data_to_encode.encode()).decode('utf-8')

        stk_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": f"Bearer {access_token}"}
        payload = {
            "BusinessShortCode": business_shortcode,
            "Password": online_password,
            "Timestamp": lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,  # Set amount to Ksh. 200
            "PartyA": phone,
            "PartyB": business_shortcode,
            "PhoneNumber": phone,
            "CallBackURL": "https://yourdomain.com/callback/",
            "AccountReference": "Book Payment",
            "TransactionDesc": "Payment for Book Purchase"
        }

        # Make the STK Push Request
        response = requests.post(stk_url, json=payload, headers=headers)
        response_data = response.json()

        if response_data.get('ResponseCode') == '0':
            return HttpResponse("STK Push successfully initiated. Check your phone to complete the payment.")
        else:
            error_message = response_data.get('errorMessage', "Something went wrong.")
            return JsonResponse({"error": error_message}, status=400)


from django.shortcuts import render
from django.http import HttpResponseBadRequest

def pay(request):
    """Renders the payment form for the selected book."""
    # Retrieve `book_id` and `action` from query parameters
    book_id = request.GET.get('book_id')
    action = request.GET.get('action')

    # Validate the presence of required parameters
    if not book_id or not action:
        return HttpResponseBadRequest("Missing required parameters: book_id or action")

    # You can also fetch the book from the database if necessary:
    # book = Book.objects.get(id=book_id)

    return render(request, 'pay.html', {
        'book_id': book_id,
        'action': action,
        # Pass book details if retrieved from the database:
        # 'book': book
    })


from django.shortcuts import render, redirect
from .forms import BookForm

def redirect_to_payment(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # Temporarily store the book details in the session
            request.session['book_data'] = form.cleaned_data
            return redirect('upload_fee')  # Redirect to payment page
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Book

def process_upload_payment(request):
    if request.method == 'POST':
        safaricom_number = request.POST.get('safaricom_number')
        book_data = request.session.get('book_data', {})

        # Validate Safaricom number
        if not safaricom_number or len(safaricom_number) != 12 or not safaricom_number.startswith('254'):
            return render(request, 'upload_fee.html', {'error': 'Please provide a valid Safaricom number.'})

        # Process payment (M-Pesa STK Push logic goes here)
        # Simulate success for now:
        payment_successful = True

        if payment_successful:
            # Save the book to the database
            Book.objects.create(
                title=book_data.get('title'),
                author=book_data.get('author'),
                genre=book_data.get('genre'),
                donor_name=book_data.get('donor_name'),
                contact_details=book_data.get('contact_details'),
                location=book_data.get('location'),
                delivery_option=book_data.get('delivery_option'),
                cover_image=book_data.get('cover_image'),
                document=book_data.get('document'),
            )
            # Clear session data after saving
            request.session.pop('book_data', None)
            return redirect('book_exchange')  # Redirect to the book exchange page
        else:
            return render(request, 'upload_fee.html', {'error': 'Payment failed. Please try again.'})



from django.shortcuts import render
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Fetch latest blogs first
    return render(request, 'blog.html', {'blogs': blogs})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ExchangedBook, DownloadedPDF  # Models for books

@login_required
def wallet(request):
    exchanged_books = ExchangedBook.objects.filter(user=request.user, status="Pending")
    downloaded_pdfs = DownloadedPDF.objects.filter(user=request.user)

    context = {
        'exchanged_books': exchanged_books,
        'downloaded_pdfs': downloaded_pdfs,
    }
    return render(request, 'wallet.html', context)



from django.shortcuts import render
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
from django.shortcuts import render
from .models import Blog  # Ensure Blog model is imported

def blog_list(request):
    blogs = Blog.objects.all()  # Fetch all blog posts
    return render(request, 'blog.html', {'blogs': blogs})
