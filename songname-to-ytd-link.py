from youtubesearchpython import VideosSearch
import json 
from time import sleep

try:
    with open('spotify_playlist_song-and-artist.csv', 'r') as readFile:
        for line in readFile:
            songTitle = line.strip()
            try:
                videosSearch = VideosSearch(songTitle, limit = 1)
                data = videosSearch.result()
            except:
                print('error trying to search youtube')
                sleep(1)
                continue


            details = (json.dumps(data, indent=4, sort_keys=True)) #can be used to print all the details coming 

            json_obj = json.loads(details)
            link = json_obj['result'][0]['link']
            try:
                with open('song_ytd_links.txt', 'a') as writeFile:
                    writeFile.write(link+'\n')
            except:
                print('error tring to write to the file')
                continue
except:
    print('error with the songname-to-ytd file')








