from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': [{'name': book.name, 'author': book.author, 'pub_date': book.pub_date} for book in books]
            }
    return render(request, template, context)


def book_info(request, pub_date):
    template = 'books/book_info.html'
    books_object = get_object_or_404(Book, pub_date=pub_date)
    try:
        previous_object = books_object.get_previous_by_pub_date()
    except:
        previous_object = None
    try:
        next_object = books_object.get_next_by_pub_date()
    except:
        next_object = None
    context = {
        'book': books_object,
        'previous': previous_object,
        'next': next_object
    }
    return render(request, template, context)
