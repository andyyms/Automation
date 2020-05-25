from bs4 import BeautifulSoup
import requests
import re
import os

class Instagram:
    def __init__(self, url):
        self.URL = url

    def parse_data(self, content):
        data = {}
        followers = re.findall("([\d]+) Followers", content)[0]
        following = re.findall("([\d]+) Following", content)[0]
        posts = re.findall("([\d]+) Posts", content)[0]

        data['Followers'] = followers
        data['Following'] = following
        data['Posts'] = posts
        return data

    def scrape_data(self, username):
        r = requests.get(self.URL.format(username))
        s = BeautifulSoup(r.text, 'html.parser')
        meta = s.find('meta', property='og:description')
        return self.parse_data(meta.attrs['content'])


if __name__ == '__main__':
    URL = 'https://www.instagram.com/{}/'
    ins = Instagram(URL)
    # Hardcode instead if you do not have .env file to store this attribute
    username = os.getenv('INS_USERNAME')
    data = ins.scrape_data(username)

    print(f'This account has {data["Followers"]} followers')
    print(f'This account has {data["Following"]} following')
    print(f'This account has {data["Posts"]} post')


