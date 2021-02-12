from django.test import SimpleTestCase
from django.urls import resolve, reverse
from tracks.views import home


class TestUrls(SimpleTestCase):

    def test_track_is_resolves(self):
        url = reverse('track')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)
