from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_catalog(request):
    template = 'books/books_list_new.html'
    list_books = []
    for object in Book.objects.all():
        object.pub_date = object.pub_date.strftime('%Y-%m-%d')
        list_books.append(object)
    context = {'books': list_books}
    return render(request, template, context)


def book_instance(request, data):
    # page_number = int(request.GET.get("page", 1))
    # paginator = Paginator(object_list, 10)
    # page = paginator.get_page(page_number)
    pass
