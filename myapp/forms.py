from django import forms
from .models import Book, Pledge, BookClub, BookDonation



from django import forms
from .models import BookClub

class BookClubForm(forms.ModelForm):
    class Meta:
        model = BookClub
        fields = ['school_name', 'county', 'students_count', 'patron_name', 'patron_contact']
        widgets = {
            'school_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 5px; padding: 10px;',
                'placeholder': 'Enter School Name'
            }),
            'county': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 5px; padding: 10px;',
                'placeholder': 'Enter County'
            }),
            'students_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 5px; padding: 10px;',
                'placeholder': 'Enter Number of Students'
            }),
            'patron_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 5px; padding: 10px;',
                'placeholder': 'Enter Patron Name'
            }),
            'patron_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 5px; padding: 10px;',
                'placeholder': 'Enter Patron Contact'
            }),
        }


class BookDonationForm(forms.ModelForm):
    class Meta:
        model = BookDonation
        fields = ['donor_name', 'donor_email', 'book_title', 'book_type', 'delivery_option', 'book_image']





from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']  # Fields from the Message model
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'style': 'border-radius: 5px; padding: 10px; font-size: 1rem;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'style': 'border-radius: 5px; padding: 10px; font-size: 1rem;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 5,
                'style': 'border-radius: 5px; padding: 10px; font-size: 1rem;'
            }),
        }



from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'title', 'message', 'photo']  # Fields included in the form
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name',
                'style': 'border-radius: 5px; padding: 10px; font-size: 1rem;'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Title (e.g., Avid Reader)',
                'style': 'border-radius: 5px; padding: 10px; font-size: 1rem;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Testimonial',
                'rows': 4,
                'style': 'border-radius: 5px; padding: 10px; font-size: 1rem;'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border-radius: 5px; padding: 10px;'
            }),
        }



from .models import Impact

class ImpactForm(forms.ModelForm):
    class Meta:
        model = Impact
        fields = '__all__'



from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


# forms.py
from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-0 w-100 py-3 pe-5',
                'placeholder': 'Email address to Subscribe',
                'style': 'background-color: #F5F5F5; color: #333333;'
            })
        }


from django import forms


class PaymentForm(forms.Form):
    safaricom_number = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Safaricom Number, e.g., +254712345678',
            'class': 'form-control',
        }),
        help_text="Phone number must start with +254 and have 13 characters.",
    )
    book_id = forms.IntegerField(widget=forms.HiddenInput())
    action = forms.ChoiceField(
        choices=[('download', 'Download'), ('exchange', 'Exchange')],
        widget=forms.HiddenInput(),
    )

    def clean_safaricom_number(self):
        """
        Validate and format the safaricom_number field.
        """
        safaricom_number = self.cleaned_data.get('safaricom_number')

        if safaricom_number.startswith('0'):
            safaricom_number = '+254' + safaricom_number[1:]
        elif safaricom_number.startswith('254'):
            safaricom_number = '+254' + safaricom_number[3:]
        elif not safaricom_number.startswith('+254'):
            raise forms.ValidationError("Invalid Safaricom number format. Ensure it starts with +254.")

        # Ensure the number is 13 characters long
        if len(safaricom_number) != 13:
            raise forms.ValidationError("Phone number must have 13 characters including +254.")

        return safaricom_number


from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import base64
from .models import Book

def submit_upload(request):
    """Handles book upload and payment process."""
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        safaricom_number = request.POST.get('safaricom_number')

        # Validate data
        if not title or not author or not genre or not safaricom_number:
            return JsonResponse({"error": "Missing required fields"}, status=400)

        # Validate phone number
        if len(safaricom_number) != 12 or not safaricom_number.startswith('254'):
            return JsonResponse({"error": "Invalid phone number. Ensure it starts with 254 and is 12 digits long."}, status=400)

        # Initiate M-Pesa payment (Ksh. 20)
        amount = 20
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'
        access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        r = requests.get(access_token_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        access_token = json.loads(r.text).get('access_token')

        lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
        business_shortcode = "174379"
        passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        data_to_encode = business_shortcode + passkey + lipa_time
        online_password = base64.b64encode(data_to_encode.encode()).decode('utf-8')

        stk_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": f"Bearer {access_token}"}
        payload = {
            "BusinessShortCode": business_shortcode,
            "Password": online_password,
            "Timestamp": lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": safaricom_number,
            "PartyB": business_shortcode,
            "PhoneNumber": safaricom_number,
            "CallBackURL": "https://yourdomain.com/payment-callback/",
            "AccountReference": "Book Upload",
            "TransactionDesc": "Upload Fee"
        }

        response = requests.post(stk_url, json=payload, headers=headers)
        response_data = response.json()

        if response_data.get('ResponseCode') == '0':
            # Temporarily store book details until payment is confirmed
            request.session['book_data'] = {'title': title, 'author': author, 'genre': genre}
            return HttpResponseRedirect(reverse('book_exchange'))
        else:
            error_message = response_data.get('errorMessage', "Something went wrong.")
            return JsonResponse({"error": error_message}, status=400)

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'genre', 'donor_name',
            'contact_details', 'location', 'delivery_option',
            'cover_image', 'document'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'donor_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'contact_details': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email or phone number',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City or town',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'delivery_option': forms.Select(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'document': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
        }


class SafaricomPaymentForm(forms.Form):
    safaricom_number = forms.CharField(
        max_length=12,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Safaricom Number (e.g., 2547XXXXXXXX)',
            'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
        })
    )

    def clean_safaricom_number(self):
        number = self.cleaned_data['safaricom_number']
        if not number.startswith('254') or len(number) != 12:
            raise forms.ValidationError('Enter a valid Safaricom number starting with 254.')
        return number


from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

from django import forms
from .models import PledgedBook

class PledgedBookForm(forms.ModelForm):
    class Meta:
        model = PledgedBook
        fields = ['donor_name', 'donor_email', 'book_title', 'book_type']

        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'donor_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'book_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'book_type': forms.Select(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import FeaturedBook

class FeaturedBookForm(forms.ModelForm):
    class Meta:
        model = FeaturedBook
        fields = ['title', 'author', 'description', 'cover_image', 'contact_email']
