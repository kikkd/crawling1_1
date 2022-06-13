import requests

res = requests.get("https://www.naver.com/")
print(res.text)

## get : 요청
## set : 생성
## put : 수정
## delete : 삭제

### GET / HTML1.1
### Host : https://www.naver.com/