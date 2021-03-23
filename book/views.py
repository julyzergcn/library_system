from django.shortcuts import render, redirect, resolve_url

from .models import Book, Publisher, Author
from .forms import BookForm,BookFormSet


# def book_list(request):
#     '''select all books from database'''
#     book_list = Book.objects.all().filter(is_deleted=False)
#     context = {
#         'books': book_list,
#     }
#     return render(request, 'book/index.html', context)


def del_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    # book_obj.delete()
    book_obj.is_deleted = True
    book_obj.save()
    return redirect('book:index')


# def edit_book(request, pk):
#     book_obj = Book.objects.filter(is_deleted=False).get(id=pk)

#     if request.method == 'POST':
#         book_obj = Book.objects.get(id=pk)
#         form = BookForm(data=request.POST, instance=book_obj)
#         if form.is_valid():
#             # save form data
#             form.save()
#             return redirect(resolve_url('book:edit_book', pk))

#     else:  # request.method == 'GET'
#         form = BookForm(instance=book_obj)

#     context = {
#         'book_obj': book_obj,
#         'form': form,
#     }
#     return render(request, 'book/modify_book.html', context)


def add_book(request): 
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            # book_name = form.cleaned_data.get('book_name')
            # price = form.cleaned_data.get('price')
            # author = form.cleaned_data.get('author')
            # publisher = form.cleaned_data.get('publisher')
            form.save()
            book_formset = BookFormSet(request.POST)
            if book_formset.is_valid():
                book_formset.save()
            # return redirect(resolve_url('book:add_book'))
            return redirect(resolve_url('book:index'))
    else:
        form = BookForm() 
        book_formset = BookFormSet()       
    context = {
        'form': form,
        'book_formset': book_formset
    }    
    # return render(request,'book/add_book.html', context)
    return render(request,'book/index.html', context)


def edit_book(request, pk):
    book_obj = Book.objects.filter(is_deleted=False).get(id=pk)

    if request.method == 'POST':
        book_obj = Book.objects.get(id=pk)
        form = BookForm(data=request.POST, instance=book_obj)
        if form.is_valid():
            # save form data
            book = form.save()
            book_formset = BookFormSet(request.POST)
            if book_formset.is_valid():
                book_formset.save()
            return redirect(resolve_url('book:edit_book', pk))

    else:  # request.method == 'GET'
        form = BookForm(instance=book_obj)
        book_formset = BookFormSet()

    context = {
        'book_obj': book_obj,
        'form': form,
        'book_formset': book_formset
    }
    return render(request, 'book/modify.html', context)
    # return render(request, 'book/index.html', context)


def book_list(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            # save form data
            book = form.save()
            book_formset = BookFormSet(request.POST)
            if book_formset.is_valid():
                book_formset.save()
            return redirect(resolve_url('book:index'))

    else:  # request.method == 'GET'
        form = BookForm()
        book_formset = BookFormSet()

    context = {
        'form': form,
        'formset': book_formset
    }
    return render(request, 'book/index.html', context)