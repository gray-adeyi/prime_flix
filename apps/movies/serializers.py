from rest_framework import serializers
from apps.movies.models import Genre, Movie, MovieVideo, Series, SeriesVideo


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = Genre


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = Movie


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = Series


class MovieVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = MovieVideo


class SeriesVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = SeriesVideo
