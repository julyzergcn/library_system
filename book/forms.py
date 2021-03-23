from django import forms
from djangoformsetjs.utils import formset_media_js

from .models import Author, Book, Publisher


class BookForm(forms.ModelForm):
    # name = forms.CharField()
    # price = forms.CharField()
    # author = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    # publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'book_name', 'price', 'author', 'publisher')
        js = formset_media_js + (

        )


BookFormSet = forms.modelformset_factory(Book, form=BookForm, extra=0)