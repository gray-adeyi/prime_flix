from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ViewTestCase(APITestCase):
    def test_get_all_movie_request_endpoint(self):
        response = self.client.get(reverse("movie-request-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
