import requests

import os
from dotenv import load_dotenv

load_dotenv() 
################################################################################

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
OUTPUT_FILE_NAME = "track_info.csv"

# change for your target playlist
PLAYLIST_LINK = 'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M'
################################################################################


