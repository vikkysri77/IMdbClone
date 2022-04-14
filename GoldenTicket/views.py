import random

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import render, redirect, get_list_or_404
from django.core.paginator import Paginator
from django_auth.users.views import *
from .forms import NewUserForm, UserForm, ProfileForm
from .models import Movie


# Create your views here.

def homepage(request):
    if request.method == "POST":
        movie_id = request.POST.get("movie_pk")
        movie = Movie.objects.get(id=movie_id)
        request.user.profile.movies.add(movie)
        messages.success(request, (f'{movie} added to wishlist.'))
        return redirect('GoldenTicket:homepage')
    movies = list(Movie.objects.all()[:6])
    movies_tr = Movie.objects.all().order_by('-movie_rating')[:6]
    movies = random.sample(movies, 6)
    return render(request=request, template_name="GoldenTicket/main.html", context={'movies': movies, 'movies_tr': movies_tr})

# def top_rated(request):
#     if request.method == "POST":
#         movie_id = request.POST.get("movie_pk")
#         movie = Movie.objects.get(id=movie_id)
#         request.user.profile.movies.add(movie)
#         messages.success(request, (f'{movie} added to wishlist.'))
#         return redirect('GoldenTicket:homepage')
#     movies_tr = Movie.objects.all().order_by('-movie_rating')[:6]
#     return render(request=request, template_name="GoldenTicket/main.html", context={'movies_tr': movies_tr})


# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("GoldenTicket:homepage")
#     form = NewUserForm
#     return render(request=request, template_name="registration/signup.html", context={"form": form})


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
    if request.method == "POST":
        movie_id = request.POST.get("movie_pk")
        movie = Movie.objects.get(id=movie_id)
        request.user.profile.movies.add(movie)
        messages.success(request, (f'{movie} added to wishlist.'))
        return redirect('GoldenTicket:movielist')
    movie_list = Movie.objects.all().order_by('-release_year')
    paginator = Paginator(movie_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="GoldenTicket/movie_list.html", context={'movie_list': page_obj})


def moviedetail(request, movie_page):
    movie_detail = Movie.objects.get(movie_slug=movie_page)
    return render(request=request, template_name='GoldenTicket/movie_detail.html',
                  context={"movie_detail": movie_detail})


def userpage(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        elif profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your wishlist was successfully updated!')
        else:
            messages.error(request, 'Unable to complete request')
        return redirect("GoldenTicket:userpage")
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request=request, template_name="GoldenTicket/user.html", context={"user": request.user,
                                                                                    "user_form": user_form,
                                                                                    "profile_form": profile_form})

# def remove_from_cart(request):
#     if request.method == 'POST':
#         movie_id = request.POST.get("movie_pk")
#         movie = Movie.objects.get(id=movie_id)
#         # movie = get_list_or_404(Movie, id=movie_id)
#         request.user.profile.movies.remove(movie)
#         messages.success(request, f'{movie} removed from wishlist.')
#         return redirect('GoldenTicket:userpage')

def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Movie.objects.filter(Q(movie_title__icontains=query))
    return render(request=request, template_name='GoldenTicket/search.html', context={'query': query, 'results': results})

