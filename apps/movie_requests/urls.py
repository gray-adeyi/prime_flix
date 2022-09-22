from rest_framework.routers import DefaultRouter
from apps.movie_requests.views import MovieRequestViewSet

router = DefaultRouter()
router.register(r"requests", MovieRequestViewSet, basename="movie-request")

urlpatterns = router.urls
