from django import forms

from .models import Author, Publisher


class BookForm(forms.Form):
    name = forms.CharField()
    price = forms.CharField()
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())
