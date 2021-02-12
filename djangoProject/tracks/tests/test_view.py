from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.track_url = reverse('track')

    def test_home_GET_when_genre_is_none(self):
        response = self.client.get(self.track_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracks/home.html')

    def test_home_GET_when_genre_is_not_none(self):
        response = self.client.get(self.track_url, {'genre': 'pop'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracks/top_tracks.html')
