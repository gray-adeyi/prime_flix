from django.db import models


class Gender(models.TextChoices):
    Male = "male"
    Female = "female"
    NonBinary = "non-binary"


class MortalityStatus(models.TextChoices):
    Living = "living"
    Deceased = "deceased"


class Artist(models.Model):
    name = models.CharField(max_length=127)
    picture = models.ImageField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=15, choices=MortalityStatus.choices)
    nationality = models.JSONField(default=list)
    debut = models.DateField
    mortality = models.CharField(max_length=15, choices=MortalityStatus.choices)
    bio = models.TextField()

    def __str__(self):
        return self.name


class SocialNetworks(models.IntegerChoices):
    Facebook = 0
    Instagram = 1
    Twitter = 2
    TikTok = 3
    Snapchat = 4


class SocialAccount(models.Model):
    artist = models.ForeignKey(
        to="artists.Artist", on_delete=models.CASCADE, related_name="socials"
    )
    account = models.PositiveIntegerField(choices=SocialNetworks.choices)
    link = models.URLField()


class Picture(models.Model):
    artist = models.ForeignKey(
        to="artists.Artist", on_delete=models.CASCADE, related_name="pictures"
    )
    caption = models.CharField(max_length=128, blank=True)
