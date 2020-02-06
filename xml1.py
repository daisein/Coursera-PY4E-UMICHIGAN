import urllib.request, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_316181.xml'
output = urllib.request.urlopen(url).read()
tree = ET.fromstring(output)

# print(output)

total = 0

for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        print(comment.find('count').text)
        total += int(comment.find('count').text)

print(total)
