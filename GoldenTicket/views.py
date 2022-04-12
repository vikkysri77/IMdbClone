from django.shortcuts import render
from .models import Movie


# Create your views here.

def homepage(request):
    movies = Movie.objects.all()[:6]
    return render(request=request, template_name="GoldenTicket/main.html", context={'movies': movies})

def movielist(request):
    movie_list = Movie.objects.all()
    return render(request=request, template_name="GoldenTicket/movie_list.html", context={'movie_list':movie_list})
