import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/webtoon/list?titleId=819217&tab=thu"
res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a)#soup 객체에서 처음 발견되는 a element 출력
#print(soup.a.attrs) a element의 속성 정보
#print(soup.a["href"])a element 의 href 속성 "값" 정보

#print(soup.find("a", attrs={"class":"Nbtn_upload"})) class="Nbtn_upload"인 a element 찾기
#print(soup.find(attrs={"class":"Nbtn_upload"})) class="Nbtn_upload"인 어떤 element 찾기

print(soup.find_all("div", attrs={"class": "EpisodeListList__info_area--Rq03U"}))
