from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("user-agent = Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15")
#유저에이전트를 설정해줘야 진짜 사람처럼 됨
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies?hl=ko&gl=US&pli=1"
browser.get(url)

interval = 2 # 2초에 한 번씩 스크롤 내릴거임    
#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height
print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source,"lxml")


#movies = soup.find_all("div",attrs={"class":["ULeU3b neq64b,"sajkdh23847"]})리스트로 감싸서 리스트 안에 있는 것들을 조건으로 가져올 수 있음
movies = soup.find_all("div",attrs={"class":"ULeU3b neq64b"})

#browser.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz[2]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[2]/c-wiz/section/div/div/div/div/div/div[3]/button").click()

for movie in movies:
    title = movie.find("div",attrs={"class":"Epkrse"}).get_text()
    print(title)
