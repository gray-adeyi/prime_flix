from django.db import models


class Genres(models.IntegerChoices):
    Comedy = 0
    Horror = 1
    Romance = 2
    ScienceFiction = 3
    Action = 4
    Drama = 5
    Adventure = 6
    Thriller = 7
    Fantasy = 9
    Western = 9
    Documentary = 9
    Animation = 10
    Crime = 11
    RomanticComedy = 12
    Musical = 13
    FilmNoir = 14
    WarFilm = 15
    Mystery = 16
    Silent = 17
    Epic = 18
    Biopic = 19
    Sports = 20
    Disaster = 21
    Docufiction = 22


class Genre(models.Model):
    name = models.PrimaryIntegerField(choices=Genres.choices, unique=True)
    description = models.TextField()

    def __str__(self):

        return self.name


class CountryMovieIndustries(models.IntegerChoices):
    Nollywood = 0
    Hollywood = 1
    Tollywood = 2
    Kollywood = 3
    Aussiewood = 4
    Lollywood = 5
    Bollywood = 6
    Kollywood = 7
    Dhallywood = 8
    Swahiliwood = 9
    Riverwood = 10
    Chinawood = 11


class CountryMovieIndustry(models.Model):
    name = models.CharField(max_length=128)
    nickname = models.PositiveIntegerField(choices=CountryMovieIndustries.choices)
    description = models.TextField()

    def __str__(self):
        return self.name


class BaseMovie(models.Model):
    title = models.CharField(max_length=128)
    genres = models.PositiveIntegerField(choices=Genres.choices)
    industry = models.ForeignKey(
        to="movies.CountryMovieIndustry", on_delete=models.SET_NULL, null=True
    )
    release_date = models.DateField()
    synopsis = models.TextField(blank=True)

    class Meta:
        abstract = True


class Movie(BaseMovie):
    ...


class Series(BaseMovie):
    ...


class Episode:
    ...


class VideoFileFormats(models.TextChoices):
    MP4 = "mp4"
    MKV = "mkv"
    AVI = "avi"
    MOV = "mov"
    WMV = "wmv"
    AVCHD = "avchd"
    FLV = "flv"
    F4V = "f4v"
    SWF = "swf"
    WEBM = "webm"
    MPEG2 = "mpeg2"


class Video(models.Model):
    poster = models.ImageField(blank=True)
    file = models.CharField()
    format = models.CharField(max_length=15, choices=VideoFileFormats.choices)
    length = models.DecimalField(
        max_digits=8, decimal_places=2, help_text="the duration of the video"
    )
