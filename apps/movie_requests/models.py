from django.db import models
from django.urls import reverse


class RequestStatus(models.IntegerChoices):
    """
    An enum with variants of all the possible states a movie request could
    be.
    """

    Pending = 0
    Fulfilled = 1
    Discarded = 2


class Request(models.Model):
    """
    A model for representing movies currently not on the platform that
    a user is intersted in seeing
    """

    title = models.CharField(verbose_name="movie title", max_length=128)
    status = models.PositiveIntegerField(
        verbose_name="movie request status", choices=RequestStatus.choices
    )
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        ordering = ["-timestamp"]

    def get_absolute_url(self) -> str:
        return reverse("movie-request", kwargs={"pk": self.pk})
