from django.http import HttpResponseRedirect
from django.shortcuts import render
from books.models import Book
from books.forms import BookForm
from django.urls import reverse


# Create your views here.
def create(request):
    """Create a new entry for the book."""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            author = form.cleaned_data["author"]
            isbn = form.cleaned_data["isbn"]
            pages = form.cleaned_data["pages"]
            year = form.cleaned_data["year"]
            b1 = Book.objects.create(
                name=name,
                author=author,
                isbn=isbn,
                pages=pages,
                year=year,
            )
            b1.save()
        return HttpResponseRedirect(reverse("book_list"))
    form = BookForm()
    return render(request, "books/create.html", {"form": form})


def update(request, book_id):
    """Update the book records."""
    current_book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            current_book.name = form.cleaned_data["name"]
            current_book.author = form.cleaned_data["author"]
            current_book.isbn = form.cleaned_data["isbn"]
            current_book.pages = form.cleaned_data["pages"]
            current_book.year = form.cleaned_data["year"]
            current_book.save()
        return HttpResponseRedirect(reverse("book_list"))
    form = BookForm(
        initial={
            "name": current_book.name,
            "author": current_book.author,
            "isbn": current_book.isbn,
            "pages": current_book.pages,
            "year": current_book.year,
        }
    )

    return render(request, "books/update.html", {"form": form})


def delete(request, book_id):
    """Delete a book record from the system."""
    current_book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        current_book.delete()
        return HttpResponseRedirect(reverse("book_list"))
    return render(request, "books/delete.html",{"book":current_book} )


def list(request):
    """Retrieve all the books listed in the system."""
    books = Book.objects.all()
    return render(request, "books/list.html", {"books": books})
