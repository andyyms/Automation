import urllib, json
from selenium import webdriver
import time

def look_for_new_video():
    api_key = ''
    channel_id = 'UCV0qA-eDDICsRR9rPcnG7tw'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = base_search_url + f'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1'
    inp = urllib.urloppen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']

    video_exist = False
    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:
            driver = webdriver.chrome()
            driver.get(base_video_url + vidID)
            video_exist = True

    if video_exist:
        with open('videoid.json', 'w') as json_file:
            data = {'videoId' : vidID}
            json.dump(data, json_file)


try:
    while True:
        look_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('stopping')
