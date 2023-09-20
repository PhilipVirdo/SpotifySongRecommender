import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
client_credentials_manager = SpotifyClientCredentials(client_id='insert client ID', client_secret='inserrt client secret')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def recommend_music(artistName):
    # Search for the artist
    searchResult = sp.search(q='artist:' + artistName, type='artist', limit = 1)

    if searchResult['artists']['total'] > 0:
        artist = searchResult['artists']['items'][0]['name']
        artistID = searchResult['artists']['items'][0]['id']
    else:
        return None, None

    # Fetch artist's music
    topTracks = sp.artist_top_tracks(artistID)['tracks']

    # Randomly select 5 tracks from the top 25 tracks
    selected = random.sample(topTracks[:25], 5)
    trackNames = [track['name'] for track in selected]

    return artist, trackNames

userInput = input("Please enter an artist: ")
newArtist, newTracks = recommend_music(userInput)

if newArtist:

    print(f"Here are 5 popular songs from {newArtist}:")

    for song in newTracks:

        print(f"- {song}")

else:

    print("Error. Check your spelling or please try another artist.")