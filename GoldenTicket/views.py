from django.shortcuts import render
from django.core.paginator import Paginator
from django_auth.users.views import *
from .models import Movie


# Create your views here.

def homepage(request):
    movies = Movie.objects.all()[:6]
    return render(request=request, template_name="GoldenTicket/main.html", context={'movies': movies})


def movielist(request):
    movie_list = Movie.objects.all()
    return render(request=request, template_name="GoldenTicket/movie_list.html", context={'movie_list': movie_list})


def movies(request):
    Movies = Movie.objects.all()
    paginator = Paginator(Movies, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="GoldenTicket/movie_list.html", context={'page_obj': page_obj})


Paginator = (movies, 20)
