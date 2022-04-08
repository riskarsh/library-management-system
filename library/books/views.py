from django.http import HttpResponseRedirect
from django.shortcuts import render
from books.models import Book
from books.forms import BookForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def create(request):
    """Create a new entry for the book.

    :param request: Django request object
    """
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
    else:
        form = BookForm()
    return render(request, "books/create.html", {"form": form})


@login_required
def update(request, book_id):
    """Update the book records.

    :param request:Django request object
    :param book_id: id of the book to update
    :type book_id: int
    """
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
    else:
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


@login_required
def delete(request, book_id):
    """Delete a book record from the system.

    :param request:Django request object
    :param book_id: id of the book to update
    :type book_id: int
    """
    current_book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        current_book.delete()
        return HttpResponseRedirect(reverse("book_list"))
    return render(request, "books/delete.html", {"book": current_book})


def list(request):
    """Retrieve all the books listed in the system.

    :param request:Django request object
    """
    books = Book.objects.all()
    return render(request, "books/list.html", {"books": books})
