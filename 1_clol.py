import requests as req

### IP 주소 알아보기
### https://api.ipify.org/ -> 내 IP알 수 있는 url

res = req.get("https://api.ipify.org/", headers={"fast":"campus"})
print(res.status_code) #200
print(res.text)

print(res.request.method)
print(res.request.headers)

print(res.elapsed) # 실행시간
print(res.raw) #바이트값을 보여줌 -> 바이트는 이미자나 동영상등 글로 표현 못하는 데이터를 바이트값을 이용해 사용함