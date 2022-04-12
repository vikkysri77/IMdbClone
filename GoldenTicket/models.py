from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    movie_poster = models.ImageField(upload_to="images", default="../static/default_avatar.png", blank=True)
    movie_rating = models.FloatField(default=False)
    #description = models.TextField()

    def __str__(self):
        return self.movie_title



