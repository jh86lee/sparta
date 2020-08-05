import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime
client = MongoClient('localhost', 27017)
db = client.dbsparta

date = datetime.today().strftime('%Y%m%d')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd='+date, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# 아래 빈 칸('')을 채워보세요
#print(datetime.today().strftime('%Y%m%d'))

for tr in trs:
    rank = tr.select_one('.number').text[0:2].strip()
    title = tr.select_one('.title').text.strip()
    artist = tr.select_one('.artist').text
    print(rank, title, artist)
    doc = {
        'rank': rank,
        'title': title,
        'artist': artist
    }
    db.musicRank.insert_one(doc)