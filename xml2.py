from bs4 import BeautifulSoup
import requests

url = 'http://py4e-data.dr-chuck.net/comments_316181.xml'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
count = soup.find_all('count')

total =  sum(int(i.text) for i in count)
print(f'The sum of all count in doc are: {total}')
