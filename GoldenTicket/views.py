from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django_auth.users.views import *
from .forms import NewUserForm
from .models import Movie


# Create your views here.

def homepage(request):
    movies = Movie.objects.all()[:6]
    return render(request=request, template_name="GoldenTicket/main.html", context={'movies': movies})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successful registration!")
            return redirect("GoldenTicket:homepage")
        messages.error(request, "Invalid info. Try again.")
    form = NewUserForm
    return render(request=request, template_name="registration/signup.html", context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("GoldenTicket:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"form": form})


def logout_request(request):
    logout(request)
    messages.success(request, "Logged Out!")
    return redirect('GoldenTicket:homepage')


def movielist(request):
    movie_list = Movie.objects.all().order_by('-release_year')
    paginator = Paginator(movie_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="GoldenTicket/movie_list.html", context={'movie_list': page_obj})

def moviedetail(request, movie_page):
    movie_detail = Movie.objects.get(movie_slug=movie_page)
    return render(request=request, template_name='GoldenTicket/movie_detail.html', context={"movie_detail": movie_detail})



# def movies(request):
#     Movies = Movie.objects.all()
#     paginator = Paginator(Movies, 20)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request=request, template_name="GoldenTicket/movie_list.html", context={'page_obj': page_obj})
#
#
# Paginator = (movies, 20)
