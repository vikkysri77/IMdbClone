from django.shortcuts import render
from .models import Movie


# Create your views here.

def movies(request):
    movies = Movie.objects.all()
    return render(request=request, template_name="GoldenTicket/main.html", context={'movies': movies})
