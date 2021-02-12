from django.test import SimpleTestCase
from tracks.genre_form import GenreForm


class TestForms(SimpleTestCase):

    def test_genre_form_valid_data(self):
        form = GenreForm(data={'genre': 'pop'})
        self.assertTrue(form.is_valid())

    def test_genre_form_not_valid_data(self):
        form = GenreForm(data={'genre': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_genre_form_data_length_bigger_than_18(self):
        form = GenreForm(data={'genre': 'aaaaaaaaaaaaaaaaaaaa'})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_genre_form_data_is_empty(self):
        form = GenreForm(data={'genre': ''})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
