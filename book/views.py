from django.shortcuts import render, redirect, resolve_url

from .models import Book, Publisher, Author
from .forms import BookForm


def book_list(request):
    '''select all books from database'''
    book_list = Book.objects.all()
    context = {
        'books': book_list,
    }
    return render(request, 'book/index.html', context)


def del_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect('book:index')


def edit_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    form = BookForm(initial={
        'name': book_obj.book_name,
        'price': book_obj.price})

    if request.method == 'POST':
        book_name = request.POST.get('name')
        book_price = request.POST.get('price')
        book_obj = Book.objects.get(id=pk)
        book_obj.book_name = book_name
        book_obj.price = book_price
        book_obj.save()
        # return redirect(request.path)
        return redirect(resolve_url('book:edit_book', pk))

    context = {
        'book_obj': book_obj,
        'form': form,
    }
    return render(request, 'book/modify_book.html', context)




