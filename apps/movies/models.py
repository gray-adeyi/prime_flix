from django.db import models

class Genres(models.IntegerChoices):
    Comedy=0
    Horror=1
    Romance=2
    ScienceFiction=3
    Action=4
    Drama=5
    Adventure=6
    Thriller=7
    Fantasy=9
    Western=9
    Documentary=9
    Animation=10
    Crime=11
    RomanticComedy=12
    Musical=13
    FilmNoir=14
    WarFilm=15
    Mystery=16
    Silent=17
    Epic=18
    Biopic=19
    Sports=20
    Disaster=21
    Docufiction=22

class Genre(models.Model):
    name = models.PrimaryIntegerField(choices=Genres.choices,unique=True)
    description = models.TextField()

    def __str__(self):

        return self.name

class CountryMovieIndustries(models.IntegerChoices):
    Nollywood=0
    Hollywood=1
    Tollywood=2
    Kollywood=3
    Aussiewood=4
    Lollywood=5
    Bollywood=6
    Kollywood=7
    Dhallywood=8
    Swahiliwood=9
    Riverwood=10
    Chinawood=11
    Unknown=12

class CountryMovieIndustry(models.Model):
    name=models.CharField(max_length=128)
    nickname=models.PositiveIntegerField(choices=CountryMovieIndustries.choices)
    description=models.TextField()

    def __str__(self):
        return self.name


class BaseMovie(models.Model):
    title
    genres
    industry
    release_date
    synopsis
