from youtubesearchpython import VideosSearch
import json 

videosSearch = VideosSearch('Flowers,Miley Cyrus', limit = 1)
data = videosSearch.result()
details = (json.dumps(data, indent=4, sort_keys=True))
json_obj = json.loads(details)
link = json_obj['result'][0]['channel']['link']
print(link)




