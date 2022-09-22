from rest_framework.routers import DefaultRouter

from apps.movies.views import GenreViewSet, MovieViewSet, SeriesViewSet

router = DefaultRouter()

router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"", MovieViewSet, basename="movie")
router.register(r"series", SeriesViewSet, basename="series")

urlpatterns = router.urls
