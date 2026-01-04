from django.shortcuts import render, redirect
from .models import Contacts, HelpQuery   
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# homepage— redirect to auth if user not logged in
def index(request):
    if not request.user.is_authenticated:
        return redirect("auth_page")
    return render(request, "pages/index.html")


def apply(request):
    if not request.user.is_authenticated:
        return redirect("auth_page")
    return render(request, "pages/apply.html")


def scheme(request):
    if not request.user.is_authenticated:
        return redirect("auth_page")
    return render(request, "pages/scheme.html")



def help_page(request):
    if not request.user.is_authenticated:
        return redirect("auth_page")

    if request.method == "POST":
        question = request.POST.get("question")
        file = request.FILES.get("fileUpload")

        HelpQuery.objects.create(
            user=request.user,
            question=question,
            file=file
        )

        messages.success(request, "Your query has been submitted successfully!")
        return redirect("help")

    return render(request, "pages/help.html")


def contact(request):
    if not request.user.is_authenticated:
        return redirect("auth_page")

    if request.method == "POST":
        print("POST:", request.POST)

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        print("MESSAGE RECEIVED:", message)

        Contacts.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, "pages/contact.html", {"success": True})

    return render(request, "pages/contact.html")


def auth_page(request):
    return render(request, "auth.html")


def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("auth_page")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please login.")
        return redirect("auth_page")

    return redirect("auth_page")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("auth_page")

    return redirect("auth_page")


def logout_user(request):
    logout(request)
    return redirect("auth_page")
