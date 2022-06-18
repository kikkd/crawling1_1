import requests as req
import re

url = "https://finance.naver.com/marketindex/"
res = req.get(url)
body = res.text # HTML 소스

#r = re.compile(r"미국 USD.*?value\">(.*?)</",re.DOTALL) # compile 함수를 통해 정규식을 미리 준비 시켜놓음
r = re.compile(r"h_lst.*?blind\">(.*?)</span.*?value\">(.*?)</",re.DOTALL) 
capture = r.findall(body)

#print(capture)
print("--------")
print("환율 계산기")
print("--------")
print("")

for c in capture:
    print(f"{c[0]} : {c[1]}")

print()
usd = float(capture[0][1].replace(",",""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력 해 주세요 : ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러 환전 되었습니다.")