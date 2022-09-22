from rest_framework import viewsets
from apps.movie_requests.serializers import MovieRequestSerializer
from apps.movie_requests.models import Request


class MovieRequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = MovieRequestSerializer
