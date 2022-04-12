from django.urls import path
from . import views

app_name = "GoldenTicket"

urlpatterns =[
    path("", views.homepage, name="homepage"),
    path("movielist/", views.movielist, name="movielist"),
]

