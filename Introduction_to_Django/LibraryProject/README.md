Django Admin Integration – Book Model

Overview

In this task, I set up the Django admin interface to manage the Book model in the bookshelf app.
The goal was to make it easier to view, search, and organize book records using Django’s built-in admin dashboard.

Steps I Followed
1. Registered the Book model

In bookshelf/admin.py, I registered the Book model with the Django admin and customized how it appears in the list view.

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')


This setup makes it possible to see key details about each book, filter by author or year, and search by title or author directly in the admin panel.

2. Defined the Book model

Here’s the Book model I used in bookshelf/models.py:

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

3. Ran migrations

After defining the model, I applied migrations to update the database:

python manage.py makemigrations
python manage.py migrate

4. Created a superuser

To access the admin panel, I created a superuser.
On Git Bash, I used:

winpty python manage.py createsuperuser


Then entered my username, email, and password.

5. Tested the admin interface

I started the development server:

python manage.py runserver


and opened the admin page at
👉 http://127.0.0.1:8000/admin/

After logging in, I could view all books, search them by title or author, and filter by publication year.

Result

The admin interface now fully supports:

Viewing book details (title, author, year)

Searching by title or author

Filtering by author and publication year

This makes managing the book data much easier and more efficient.

Folder Structure
Introduction_to_Django/
│
├── LibraryProject/
│   ├── manage.py
│   └── LibraryProject/
│       ├── settings.py
│       ├── urls.py
│       └── ...
│
└── bookshelf/
    ├── models.py
    ├── admin.py
    ├── views.py
    └── ...

Summary

This task helped me understand how Django’s admin interface works and how to customize it for better usability.
By registering the Book model and adding filters, search fields, and list displays, I made the admin panel more intuitive for managing book data.
