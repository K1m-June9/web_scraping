import requests
url="http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)


res.raise_for_status() # 위와 함께 이것도 같이 씀(정상 작동 시 계속 진행
print("응답코드: ",res.status_code) #200이면 정상


print(len(res.text))
with open("nadocoding.html","w", encoding="utf-8") as f:
    f.write(res.text)