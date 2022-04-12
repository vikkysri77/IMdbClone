from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to="images/")
    screen_shots = models.ImageField(upload_to="screenshots/")
    movie_length = models.CharField(max_length=50)
    release_date = models.DateField()
    movie_rate = models.CharField(max_length=100)
    imdb_rating = models.CharField(max_length=100)
    movie_actor = models.CharField(max_length=100)




