import requests

import os
from dotenv import load_dotenv

import csv
import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() 
################################################################################

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
OUTPUT_FILE_NAME = "track_info.csv"

# change for your target playlist
PLAYLIST_LINK = 'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=b17f987ba59f490a'
################################################################################


# authenticate
client_credentials_manager = SpotifyClientCredentials(
                                            client_id=CLIENT_ID, 
                                            client_secret=CLIENT_SECRET)

# create spotify session object
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# get uri from https link
if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", PLAYLIST_LINK):
    playlist_uri = match.groups()[0]
else:
    raise ValueError("Please add complete link to PLAYLIST_LINK (copy from app, not the web): Expected format: https://open.spotify.com/playlist/...")







