from multiprocessing import AuthenticationError
from django import forms


class BookForm(forms.Form):
    name = forms.CharField(label="name", max_length=50)
    author = forms.CharField(label="author")
    isbn = forms.IntegerField(label="isbn")
    pages = forms.IntegerField(label="Pages")
    year = forms.IntegerField(label="year")
