from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from django_auth.users.models import *


# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    movie_poster = models.ImageField(upload_to="images", default="../static/default_avatar.png", blank=True)
    movie_bg = models.ImageField(upload_to="background", default="../static/default_avatar.png", blank=True)
    movie_rating = models.FloatField(default=False)
    movie_desc = models.TextField(default=False)
    movie_slug = models.SlugField(max_length=200, blank=True, null=True)
    affiliate_url = models.SlugField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.movie_title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
