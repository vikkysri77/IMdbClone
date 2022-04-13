from django.urls import path
from . import views

app_name = "GoldenTicket"
app_name = "users"

urlpatterns =[
    path("", views.homepage, name="homepage"),
    path("movielist/", views.movielist, name="movielist"),
    path("home/", views.home, name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]

