from turtle import title
from urllib import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from apps.movie_requests.models import Request, RequestStatus


class ViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request_obj = Request.objects.create(
            title="test movie request", status=RequestStatus.Pending
        )

    def test_get_all_movie_request_endpoint(self):
        response = self.client.get(reverse("movie-request-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movie_request_endpoint(self):
        response = self.client.get(
            reverse("movie-request-detail", kwargs={"pk": self.request_obj.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
