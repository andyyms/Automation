import re

s = '<meta content="0 Followers, 11 Following, 64 Posts - See Instagram photos and videos from @andyyms.tech" property="og:description"/>'

followers = re.findall("([\d]+) Followers", s)[0]
following = re.findall("([\d]+) Following", s)[0]
posts = re.findall("([\d]+) Posts", s)[0]

print(f'followers: {followers} ')
print(f'following: {following}')
print(f'posts: {posts}')



