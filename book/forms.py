from django import forms


class BookForm(forms.Form):
    name = forms.CharField()
    price = forms.CharField()
