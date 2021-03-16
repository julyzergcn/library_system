from django import forms

from .models import Author, Book, Publisher


class BookForm(forms.ModelForm):
    # name = forms.CharField()
    # price = forms.CharField()
    # author = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    # publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ('book_name', 'price', 'author', 'publisher')
