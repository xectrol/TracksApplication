import json
import random

import requests
from tracks.constant import constants


def get_most_popular_tracks(genre):
    url = constants.GET_MOST_POPULAR_TRACKS_URL.format(get_artist_id(pick_random_artist(genre)))
    response = requests.get(url, headers={constants.CONTENT_TYPE: constants.APPLICATION_JSON,
                                          constants.AUTHORIZATION: "Bearer {}".format(get_access_token())})
    print(response)
    tracks = response.json()[constants.TRACKS]
    track_info_list = list()

    for x in range(5):
        if x not in track_info_list:
            track_infos = dict()
            track_infos[constants.ARTIST] = tracks[x][constants.ARTISTS][0][constants.NAME]
            track_infos[constants.TRACK] = tracks[x][constants.NAME]
            track_infos[constants.ALBUM_URL] = tracks[x][constants.ALBUM][constants.IMAGES][0][constants.URL]
            track_infos[constants.RELEASE_DATE] = tracks[x][constants.ALBUM][constants.RELEASE_DATE]
            track_info_list.append(track_infos)

    return track_info_list


def get_artist_id(artist_name):
    url = constants.GET_ARTISTS_ID_URL.format(artist_name)
    response = requests.get(url, headers={constants.CONTENT_TYPE: constants.APPLICATION_JSON,
                                          constants.AUTHORIZATION: "Bearer {}".format(get_access_token())})
    input_dict = response.json()
    return input_dict[constants.ARTISTS][constants.ITEMS][0][constants.ID]


def get_access_token():
    url = constants.ACCESS_TOKEN_URL
    body = constants.ACCESS_TOKEN_REQUEST_BODY
    headers = {
        constants.CONTENT_TYPE: constants.FORM_URL_ENCODED,
        constants.AUTHORIZATION: constants.BASIC_TOKEN,
    }

    response = requests.request("POST", url, data=body, headers=headers)

    json_obj = response.json()
    return json_obj[constants.ACCESS_TOKEN]


def pick_random_artist(genre):
    filepath = open(r'D:\test\djangoProject\genre.json')
    # parse file
    data = json.load(filepath)
    artists = data[genre]
    try:
        artist = random.choice(artists)
        print(artist)
        return artist
    except IndexError:
        print("Nothing found")
