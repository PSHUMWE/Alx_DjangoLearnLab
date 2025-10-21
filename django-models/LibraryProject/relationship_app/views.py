from django.shortcuts import render
from django.views import View
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


# Class-based view to display details for a specific library
class LibraryDetailView(View):
    def get(self, request, library_id):
        library = Library.objects.get(id=library_id)
        return render(request, 'library_detail.html', {'library': library})

