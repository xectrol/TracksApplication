from django.shortcuts import render

from tracks.genre_form import GenreForm
from tracks.spotify_api import get_most_popular_tracks


def home(request):
    genre = request.GET.get('genre', None)

    if genre is not None and genre != '':
        form = GenreForm(request.GET)
        if form.is_valid():
            tracks = get_most_popular_tracks(genre)
            context = {
                'tracks': tracks
            }
            return render(request, 'tracks/top_tracks.html', context)
        else:
            return render(request, 'tracks/home.html', {'form': form})
    else:
        return render(request, 'tracks/home.html', {'form': GenreForm()})
