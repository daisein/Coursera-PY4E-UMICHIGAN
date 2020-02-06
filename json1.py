import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_316182.json'
data = urllib.request.urlopen(url).read().decode()

js = json.loads(data)

sum = 0
for comment in js['comments']:
    sum += int(comment['count'])
print(sum)
