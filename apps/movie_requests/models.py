from django.db import models


class RequestStatus(models.IntegerChoices):
    Pending = 0
    Fulfilled = 1
    Discarded = 2


class Request(models.Model):
    title = models.CharField(verbose_name="movie title", max_length=128)
    status = models.PositiveIntegerField(choices=RequestStatus.choices)
    description = models.TextField(blank=True)
