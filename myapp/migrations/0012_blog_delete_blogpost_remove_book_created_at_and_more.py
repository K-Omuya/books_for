# Generated by Django 5.1.6 on 2025-03-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_payment_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.RemoveField(
            model_name='book',
            name='created_at',
        ),
        migrations.AddField(
            model_name='book',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='book_documents/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='contact_details',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='delivery_option',
            field=models.CharField(choices=[('Pickup', 'Pickup'), ('Courier', 'Courier')], max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='donor_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Science', 'Science'), ('Biography', 'Biography')], max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
