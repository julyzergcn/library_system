from django.urls import path
from book import views

app_name = 'book'
urlpatterns = [
    path('index/',views.book_list,name="index"),
    path('del_book/',views.del_book,name="del_book"),
    path('edit_book/',views.edit_book,name="edit_book"),
    path('edit_book_logic/',views.edit_book_logic,name="edit_book_logic"),
]