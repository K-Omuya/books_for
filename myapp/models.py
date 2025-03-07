from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book_images/')
    book_type = models.CharField(
        max_length=50,
        choices=[('curriculum', 'Curriculum'), ('storybook', 'Storybook'), ('general', 'General Reading')]
    )
    drop_off_location = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

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

class Book(models.Model):
    GENRES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('History', 'History'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('Biography', 'Biography'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRES)
    donor_name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    delivery_option = models.CharField(
        max_length=50,
        choices=[('Drop Off', 'Drop Off Location'), ('Pick Up', 'Personal Pick Up')]
    )
    cover_image = models.ImageField(upload_to='book_covers/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


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
