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
    Western = 10
    Documentary = 11
    Animation = 12
    Crime = 13
    RomanticComedy = 14
    Musical = 15
    FilmNoir = 16
    WarFilm = 17
    Mystery = 18
    Silent = 19
    Epic = 20
    Biopic = 21
    Sports = 22
    Disaster = 23
    Docufiction = 24


class Genre(models.Model):
    name = models.PositiveIntegerField(
        choices=Genres.choices, unique=True, help_text="the name of the movie genre"
    )
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.name)


class CountryMovieIndustries(models.IntegerChoices):
    Nollywood = 0
    Hollywood = 1
    Tollywood = 2
    Kollywood = 3
    Aussiewood = 4
    Lollywood = 5
    Bollywood = 6
    Dhallywood = 7
    Swahiliwood = 8
    Riverwood = 9
    Chinawood = 10


class CountryMovieIndustry(models.Model):
    name = models.CharField(
        max_length=128,
        help_text="the category a move belongs to based on it's country of origin",
    )
    nickname = models.PositiveIntegerField(choices=CountryMovieIndustries.choices)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.name)


class BaseMovie(models.Model):
    title = models.CharField(max_length=128)
    genres = models.PositiveIntegerField(choices=Genres.choices)
    industry = models.ForeignKey(
        to="movies.CountryMovieIndustry", on_delete=models.SET_NULL, null=True
    )
    release_date = models.DateField()
    synopsis = models.TextField(blank=True)
    cast = models.ManyToManyField(to="artists.Artist")
    timestamp = models.DateTimeField(
        auto_now_add=True, help_text="the date and time the movie was created"
    )

    class Meta:
        abstract = True


class Movie(BaseMovie):
    ...


class Series(BaseMovie):
    class Meta:
        verbose_name_plural = "series"


class Season(models.Model):
    series = models.ForeignKey(to="movies.Series", on_delete=models.CASCADE)
    season = models.PositiveIntegerField(default=1)


class Episode(models.Model):
    series = models.ForeignKey(to="movies.Season", on_delete=models.CASCADE)
    number = models.PositiveIntegerField(
        verbose_name="episode number", help_text="the episode's number"
    )
    summary = models.TextField(blank=True)


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
    file = models.FileField()
    format = models.CharField(max_length=15, choices=VideoFileFormats.choices)
    length = models.DecimalField(
        max_digits=8, decimal_places=2, help_text="the duration of the video"
    )

    class Meta:
        abstract = True


class MovieVideo(Video):
    movie = models.OneToOneField(
        to="movies.Movie", related_name="video", on_delete=models.CASCADE
    )


class SeriesVideo(Video):
    series = models.ForeignKey(
        to="movies.Series", related_name="videos", on_delete=models.CASCADE
    )
