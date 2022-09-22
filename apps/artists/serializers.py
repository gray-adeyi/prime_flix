from dataclasses import field
from rest_framework import serializers
from apps.artists.models import Artist, Picture, SocialAccount


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = Artist


class SocialAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = SocialAccount


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = Picture
