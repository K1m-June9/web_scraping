from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



browser = webdriver.Chrome(options=chrome_options)


#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
elem.click()

# 3. id, pw입력
browser.find_element(By.ID,"id").send_keys("naverID")
browser.find_element(By.ID,"pw").send_keys("pwww")

#4. 로그인 버튼 클릭
browser.find_element(By.ID,"log.login").click()
time.sleep(3)

#5. id를 새로 입력
browser.find_element(By.ID,"id").clear() #기존에 썼던 값 중복 안되게 없앰
browser.find_element(By.ID,"id").send_keys("IDIDIDID")

#6. html 정보 출력
print(browser.page_source)

#7. 브라우저 종료
browser.close()#현재 탭만 종료
browser.quit()# 전체 브라우저 종료
