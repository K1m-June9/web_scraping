from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



browser = webdriver.Chrome(options=chrome_options)


url = "https://flight.naver.com/"
browser.get(url)

browser.find_element(By.XPATH,"//*[@id='__next']/div/div/div[4]/div/div/div[2]/div[2]/button[1]").click()

browser.find_element(By.XPATH, "//button[b[text()='20']]").click()
time.sleep(1)
browser.find_element(By.XPATH, "//button[b[text()='28']]").click()
#browser.find_element(By.XPATH,"//*[@id='__next']/div/div/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button")
time.sleep(1)
browser.find_element(By.XPATH,"//*[@id='__next']/div/div/div[4]/div/div/div[2]/div[1]/button[2]").click()
time.sleep(1)
browser.find_element(By.XPATH,"//*[@id='__next']/div/div/div[10]/div[2]/section/section/button[1]").click()
time.sleep(1)
browser.find_element(By.XPATH,"//*[@id='__next']/div/div/div[10]/div[2]/section/section/div/button[2]").click()
time.sleep(1)
browser.find_element(By.XPATH,"//*[@id='__next']/div/div/div[4]/div/div/div[2]/button").click()
try:
    #로딩 처리(XPATH에 위치한 어떤 엘리먼트가 위치할 때까지 10초를 기다림)
    elen = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]")))
    elem = browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]")
    print(elem.text)
finally:
    browser.quit()
#첫결과 출력
# elem = browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]")
# print(elem.text)