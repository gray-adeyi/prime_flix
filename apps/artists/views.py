from rest_framework import viewsets

from apps.artists.models import Artist
from apps.artists.serializers import ArtistSerializer


class ArtistViewSet(viewsets.ViewSet):
    queryset = Artist
    serializer_class = ArtistSerializer
