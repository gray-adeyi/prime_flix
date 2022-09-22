from rest_framework.routers import DefaultRouter

from apps.artists.views import ArtistViewSet

router = DefaultRouter()
router.register(r"", ArtistViewSet, basename="artist")

urlpatterns = router.urls
