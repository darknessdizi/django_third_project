from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_catalog(request):
    template = 'books/books_list_new.html'
    for i in Book.objects.all():
        print(i.pub_date)
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def book_instance(request):
    pass
