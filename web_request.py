import requests
res = requests.get("http://google.com") #해당 페이지에 접속하여 정보를 받아오는 것
#res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() # 위와 함께 이것도 같이 씀(정상 작동 시 계속 진행
print("응답코드: ",res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("문제 발생[ 에러코드",res.status_code,"]")

print(len(res.text))
with open("mygoogle.html","w", encoding="utf-8") as f:
    f.write(res.text)