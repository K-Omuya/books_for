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
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'genre', 'donor_name',
            'contact_email', 'contact_phone', 'location',
            'delivery_options', 'cover_image', 'document'
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
            'contact_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City or town',
                'style': 'border: 1px solid #DDD; border-radius: 6px; padding: 10px;'
            }),
            'delivery_options': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe delivery options',
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

