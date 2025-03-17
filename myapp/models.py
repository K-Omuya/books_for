# models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    GENRES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Science', 'Science'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRES)
    document = models.FileField(upload_to='books/')
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    exchange_available = models.BooleanField(default=True)
    download_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Pledge(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    book_count = models.PositiveIntegerField()
    pledged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.book_count} books"

from django.db import models

class BookClub(models.Model):
    school_name = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    students_count = models.IntegerField()
    patron_name = models.CharField(max_length=255)
    patron_contact = models.CharField(max_length=15)

    def __str__(self):
        return self.school_name



class PledgedBook(models.Model):
    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField()
    book_title = models.CharField(max_length=255)
    book_type_choices = [
        ('curriculum', 'Curriculum'),
        ('storybook', 'Storybook'),
        ('general', 'General Reading')
    ]
    book_type = models.CharField(max_length=20, choices=book_type_choices)
    pledge_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title

from django.db import models

class BookDonation(models.Model):
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    book_title = models.CharField(max_length=200)
    book_type = models.CharField(
        max_length=50,
        choices=[('curriculum', 'Curriculum'), ('storybook', 'Storybook'), ('general', 'General Reading')]
    )
    delivery_option = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='book_donations/')
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book_title} by {self.donor_name}"




from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"



from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.title}"


from django.db import models


from django.db import models

class Impact(models.Model):
    students_impacted = models.PositiveIntegerField(default=0)
    schools_reached = models.PositiveIntegerField(default=0)
    exchanges_facilitated = models.PositiveIntegerField(default=0)
    books_donated = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Impact Data: {self.students_impacted} Students, {self.schools_reached} Schools"


from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment with {self.name} on {self.date} at {self.time}"

# models.py
from django.db import models

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email





from django.utils.timezone import now  # Import this at the top

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)  # ✅ Added default

    def __str__(self):
        return self.title



# models.py
from django.db import models

class Book(models.Model):
    GENRES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Science', 'Science'),
    ]

    title = models.CharField(max_length=200)  # Mandatory
    author = models.CharField(max_length=200)  # Mandatory
    genre = models.CharField(max_length=50, choices=GENRES)  # Mandatory
    donor_name = models.CharField(max_length=200)  # Mandatory
    contact_details = models.CharField(max_length=200)  # Mandatory
    location = models.CharField(max_length=200)  # Mandatory
    delivery_option = models.CharField(
        max_length=50,
        choices=[('Drop-off', 'Drop-off'), ('Pick-up', 'Pick-up')],  # Mandatory
    )
    cover_image = models.ImageField(upload_to='cover_photos/')  # Mandatory
    document = models.FileField(upload_to='documents/', blank=True, null=True)  # Optional

    def __str__(self):
        return self.title# models.py


from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    GENRES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Science', 'Science'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRES)
    location = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='cover_photos/', blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    download_available = models.BooleanField(default=True)
    exchange_available = models.BooleanField(default=True)
    donor_name = models.CharField(max_length=100)

    # New fields
    contact_email = models.EmailField(max_length=100, blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    delivery_options = models.TextField(
        help_text="Describe the delivery options available (e.g., shipping, pickup)",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class ExchangeRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    admin_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.requester.username} -> {self.book.title}"
