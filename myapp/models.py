from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    from django.db import models

    class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=100)
        genre = models.CharField(max_length=50, choices=[
            ('Fiction', 'Fiction'),
            ('Non-Fiction', 'Non-Fiction'),
            ('Science', 'Science'),
            ('Biography', 'Biography')
        ])
        donor_name = models.CharField(max_length=100)
        contact_details = models.CharField(max_length=200)
        location = models.CharField(max_length=100)
        delivery_option = models.CharField(max_length=100, choices=[
            ('Pickup', 'Pickup'),
            ('Courier', 'Courier')
        ])
        cover_image = models.ImageField(upload_to='book_images/', null=True, blank=True)
        document = models.FileField(upload_to='book_documents/', null=True, blank=True)

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


from django.db import models

class Payment(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=20.00)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Completed", "Completed")], default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.status}"


from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=[
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science', 'Science'),
        ('Biography', 'Biography')
    ])
    donor_name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    delivery_option = models.CharField(max_length=100, choices=[
        ('Pickup', 'Pickup'),
        ('Courier', 'Courier')
    ])
    cover_image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    document = models.FileField(upload_to='book_documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the current date/time when a record is created

    def __str__(self):
        return self.title
