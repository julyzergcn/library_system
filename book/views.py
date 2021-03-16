from django.shortcuts import render,redirect
from .models import Book,Publisher,Author
# Create your views here.

def book_list(request):
    '''select all books from database'''
    book_list = Book.objects.all()
    return render(request,'book/index.html',{'books':book_list})

# def add_book(request):
#     if request.method == 'POST':
#         book_name = request.POST.get('name')
#         publisher_id = request.POST.get('publisher_id')
#         models.Book.objects.create(book_name=book_name,pub)

def del_book(request):
    book_id = request.GET.get('id')
    book_obj = Book.objects.get(id=book_id)
    book_obj.delete()
    return redirect('/book/index/')

def edit_book(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    price = request.GET.get('price')
    return render(request,'book/modify_book.html',{'id':id,
                                                   'name':name,
                                                   'price':price})

def edit_book_logic(request):
    if request.method == 'POST':
        book_id = request.POST.get('id')
        book_name = request.POST.get('name')
        book_price = request.POST.get('price')
        book_obj = Book.objects.get(id=book_id) 
        print(book_obj,book_id)
        book_obj.book_name = book_name
        book_obj.price = book_price
        book_obj.save()
        return redirect(reverse('book:index'))




