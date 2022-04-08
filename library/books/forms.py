from django import forms
from datetime import date


class BookForm(forms.Form):
    name = forms.CharField(label="name", max_length=50)
    author = forms.CharField(label="author")
    isbn = forms.IntegerField(label="isbn")
    pages = forms.IntegerField(label="pages")
    year = forms.IntegerField(label="year")

    def clean_year(self):
        """validation for year field"""
        data = self.cleaned_data["year"]
        today = date.today()
        year = int(today.strftime("%Y"))
        if data > year:
            raise forms.ValidationError("Published year cannot be in future")
        if data < 0:
            raise forms.ValidationError("Published year cannot be negative")
        return data

    def clean_pages(self):
        """validation for year field"""
        data = self.cleaned_data["pages"]
        if data <= 0:
            raise forms.ValidationError("Number of pages can't be 0 or less than 0")
        return data
