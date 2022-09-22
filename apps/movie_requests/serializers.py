from rest_framework import serializers
from apps.movie_requests.models import Request


class MovieRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"
        extra_kwargs = {"url": {"view_name": "movie-request-detail"}}
