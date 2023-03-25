import requests
from bs4 import BeautifulSoup

spotifyPlaylistLink = 'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M'

response = requests.get(spotifyPlaylistLink)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)
    song_list = soup.find_all("li", class_="song")

    for song in song_list:
        print(song.text)
else:
    print(f"Error: {response.status_code}")
