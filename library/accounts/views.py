from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    """View to signup library admin user.

    :param request: Django request object
    """
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            email = signup_form.cleaned_data.get("email")
            password = signup_form.cleaned_data.get("password1")
            admin = authenticate(username=email, password=password)
            login(request, admin)
            return redirect("book_list")
    else:
        signup_form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": signup_form})


def signin(request):
    """View to signin library admin user.

    :param request: Django request object
    """
    if request.method == "POST":
        email = request.POST["username"]
        password = request.POST["password"]
        admin = authenticate(username=email, password=password)
        login(request, admin)
        return redirect("book_list")
    form = AuthenticationForm()
    return render(request, "accounts/signin.html", {"form": form})


def signout(request):
    """View to signout library admin user.

    :param request: Django request object
    """
    if request.method == "POST":
        logout(request)
        return redirect("book_list")
    return render(
        request,
        "accounts/signout.html",
    )
