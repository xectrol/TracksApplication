import json
from unittest.mock import Mock

import responses

from django.test import SimpleTestCase
from tracks import spotify_api

tracks_response = {
    "tracks": [
        {
            "album": {
                "images": [{
                    "url": "https://i.scdn.co/image/ab67616d0000b2730cb9e4d49412fce4ae730004"
                }],
                "release_date": "1997-11-04"
            },
            "artists": [{
                "name": "B.B. King"
            }],
            "name": "The Thrill Is Gone"
        },
        {
            "album": {
                "images": [{
                    "url": "https://i.scdn.co/image/ab67616d0000b2730cb9e4d49412fce4ae730004"
                }],
                "release_date": "1997-11-04"
            },
            "artists": [{
                "name": "B.B. King"
            }],
            "name": "The Thrill Is Gone"
        },
        {
            "album": {
                "images": [{
                    "url": "https://i.scdn.co/image/ab67616d0000b2730cb9e4d49412fce4ae730004"
                }],
                "release_date": "1997-11-04"
            },
            "artists": [{
                "name": "B.B. King"
            }],
            "name": "The Thrill Is Gone"
        },
        {
            "album": {
                "images": [{
                    "url": "https://i.scdn.co/image/ab67616d0000b2730cb9e4d49412fce4ae730004"
                }],
                "release_date": "1997-11-04"
            },
            "artists": [{
                "name": "B.B. King"
            }],
            "name": "The Thrill Is Gone"
        },
        {
            "album": {
                "images": [{
                    "url": "https://i.scdn.co/image/ab67616d0000b2730cb9e4d49412fce4ae730004"
                }],
                "release_date": "1997-11-04"
            },
            "artists": [{
                "name": "B.B. King"
            }],
            "name": "The Thrill Is Gone"
        },
    ]
}

access_token_response = {
    'access_token': 'anyToken'
}

artist_id_response = {"artists": {
    "items": [{"id": "anyId"}]
}}


class TestSpotifyApi(SimpleTestCase):

    @responses.activate
    def test_get_access_token(self):
        responses.add(responses.POST, 'https://accounts.spotify.com/api/token',
                      body=json.dumps(access_token_response), status=200,
                      content_type='application/x-www-form-urlencoded',
                      match_querystring=False)

        response = spotify_api.get_access_token()

        assert response == access_token_response.get('access_token')
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'https://accounts.spotify.com/api/token'

    @responses.activate
    def test_get_artist_id(self):
        responses.add(responses.POST, 'https://accounts.spotify.com/api/token',
                      body=json.dumps(access_token_response), status=200,
                      content_type='application/x-www-form-urlencoded',
                      match_querystring=False)

        responses.add(responses.GET, 'https://api.spotify.com/v1/search?q=anyArtistName&type=artist',
                      body=json.dumps(artist_id_response), status=200,
                      content_type='application/json',
                      match_querystring=False)

        response = spotify_api.get_artist_id('anyArtistName')

        assert response == artist_id_response['artists']['items'][0]['id']
        assert len(responses.calls) == 2
        assert responses.calls[1].request.url == 'https://api.spotify.com/v1/search?q=anyArtistName&type=artist'

    @responses.activate
    def test_get_most_popular_tracks(self):
        responses.add(responses.POST, 'https://accounts.spotify.com/api/token',
                      body=json.dumps(access_token_response), status=200,
                      content_type='application/x-www-form-urlencoded',
                      match_querystring=False)

        responses.add(responses.GET, 'https://api.spotify.com/v1/search?q=anyArtistName&type=artist',
                      body=json.dumps(artist_id_response), status=200,
                      content_type='application/json',
                      match_querystring=False)

        responses.add(responses.GET, 'https://api.spotify.com/v1/artists/anyId/top-tracks?market=tr',
                      body=json.dumps(tracks_response), status=200,
                      content_type='application/json',
                      match_querystring=False)
        spotify_api.pick_random_artist = Mock(return_value='genre')

        spotify_api.get_most_popular_tracks(spotify_api.pick_random_artist)

        assert len(responses.calls) == 4
        assert responses.calls[3].request.url == 'https://api.spotify.com/v1/artists/anyId/top-tracks?market=tr'
