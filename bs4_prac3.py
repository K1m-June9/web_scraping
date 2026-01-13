import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/webtoon/list?titleId=819217&tab=wed"
res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("div", attrs = {"class":"EpisodeListList__meta_info--Cgquz"})
for cartoon in cartoons:
    rate = cartoon.find("span").get_text()
    print(rate)