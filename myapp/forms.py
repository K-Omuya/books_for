from django import forms
from .models import Book, Pledge, BookClub, BookDonation



class PledgedBookForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ['name', 'email', 'book_count']

from django import forms
from .models import BookClub
class BookClubForm(forms.ModelForm):
    class Meta:
        model = BookClub
        fields = ['school_name', 'county', 'students_count', 'patron_name', 'patron_contact']


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


from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'genre', 'donor_name',
            'contact_details', 'location', 'delivery_option',
            'cover_image'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'donor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'contact_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email or Phone Number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City or Town'}),
            'delivery_option': forms.Select(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
