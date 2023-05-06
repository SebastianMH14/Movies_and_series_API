from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    MOVIE = 'movie'
    SERIES = 'series'
    TYPE_CHOICES = [
        (MOVIE, 'Movie'),
        (SERIES, 'Series'),
    ]

    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default=MOVIE)
    views = models.PositiveIntegerField(default=0)
    average_rating = models.PositiveIntegerField(default=0)  # puntuacion media

    def __str__(self):
        return self.name


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_rating = models.FloatField(
        default=0)
    num_ratings = models.PositiveIntegerField(default=1)
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('movie', 'user')


class View(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view = models.BooleanField(default=False)

    class Meta:
        unique_together = ('movie', 'user')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.movie.views += 1
            self.movie.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Pelicula: {self.movie.name} | Usuario: {self.user.username} | Vista: {str(self.view)}"
