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

    if request.method == 'POST':
        book_obj = Book.objects.get(id=pk)
        form = BookForm(data=request.POST)
        if form.is_valid():
            # save form data
            book_obj.book_name = form.cleaned_data['name']
            book_obj.price = form.cleaned_data['price']
            book_obj.publisher = form.cleaned_data['publisher']
            # book_obj.author = form.cleaned_data['author']
            book_obj.save()
            book_obj.author.set(form.cleaned_data['author'])
            return redirect(resolve_url('book:edit_book', pk))

    else:  # request.method == 'GET'
        form = BookForm(initial={
            'name': book_obj.book_name,
            'price': book_obj.price,
            'publisher': book_obj.publisher,
            'author': book_obj.author.all(),
            })

    context = {
        'book_obj': book_obj,
        'form': form,
    }
    return render(request, 'book/modify_book.html', context)




