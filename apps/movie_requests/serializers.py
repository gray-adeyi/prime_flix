from apps.movie_request.models import Request


class MovieRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"
