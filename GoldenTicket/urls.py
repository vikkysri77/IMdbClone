from django.urls import path
from . import views

app_name = "GoldenTicket"

urlpatterns =[
    path("", views.movies, name="movies"),
]

