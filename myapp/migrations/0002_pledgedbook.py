# Generated by Django 5.1.6 on 2025-03-05 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PledgedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=255)),
                ('donor_email', models.EmailField(max_length=254)),
                ('book_title', models.CharField(max_length=255)),
                ('book_type', models.CharField(choices=[('curriculum', 'Curriculum'), ('storybook', 'Storybook'), ('general', 'General Reading')], max_length=20)),
                ('pledge_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
