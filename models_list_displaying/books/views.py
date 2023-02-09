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
    list_books = sorted(list_books, key=lambda i: i.pub_date)
    context = {'books': list_books}
    return render(request, template, context)


def book_instance(request, data):
    list_books = []
    next_date = None
    previous_data = None

    for object in Book.objects.all():
        object.pub_date = object.pub_date.strftime('%Y-%m-%d')
        if not list_books:
            new_dict = {'data': None, 'books': []}
            new_dict['books'].append(object)
            new_dict['data'] = object.pub_date
            list_books.append(new_dict)
            continue
        for element in list_books:
            if object.pub_date == element['data']:
                element['books'].append(object)
                break
        else:
            new_dict = {'data': None, 'books': []}
            new_dict['books'].append(object)
            new_dict['data'] = object.pub_date
            list_books.append(new_dict)

    list_books = sorted(list_books, key=lambda i: i['data'])
    for i, element in enumerate(list_books):
        if data == element['data']:
            index = i
    
    paginator = Paginator(list_books, 1)
    page = paginator.get_page(index + 1)
 
    if index != len(list_books) - 1:
        next_date = list_books[index + 1]['data'] 
    if index != 0:
        previous_data = list_books[index - 1]['data']

    context = {
                'books': page.__dict__['object_list'][0]['books'],
                'page': page,
                'next_date': next_date,
                'previous_data': previous_data,
            }  
    return render(request, 'books/books_catalog.html', context)
