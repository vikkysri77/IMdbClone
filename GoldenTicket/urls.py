from django.urls import path
from . import views

app_name = "GoldenTicket"

urlpatterns =[
    path("", views.homepage, name="homepage"),
    path("movielist/", views.movielist, name="movielist"),
    path("signup/", views.register, name="signup"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("<movie_page>", views.moviedetail, name="moviedetail"),
    path("user/", views.userpage, name="userpage"),
    # path("del/", views.remove_from_cart, name="del")

]

