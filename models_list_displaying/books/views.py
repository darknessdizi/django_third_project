from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_catalog(request):
    template = 'books/books_catalog.html'
    list_books = []
    for object in Book.objects.all():
        object.pub_date = object.pub_date.strftime('%Y-%m-%d')
        list_books.append(object)
    context = {'books': list_books}
    return render(request, template, context)


def book_instance(request, data):
    list_books = []
    list_data = []
    next_date = None
    previous_data = None

    for object in Book.objects.all():
        object.pub_date = object.pub_date.strftime('%Y-%m-%d')
        list_books.append(object)
        list_data.append(object.pub_date)

    index = list_data.index(data)

    paginator = Paginator(list_books, 1)
    page = paginator.get_page(index + 1)

    if index != len(list_data) - 1:
        next_date = list_data[index + 1]
    if index != 0:
        previous_data = list_data[index - 1]

    context = {
                'books': page,
                'page': page,
                'next_date': next_date,
                'previous_data': previous_data,
            }  
    return render(request, 'books/books_catalog.html', context)
