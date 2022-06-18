import requests as req
from bs4 import BeautifulSoup as BS

# url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
# print(res.text)
soup = BS(res.text,"html.parser")

tds = soup.find_all("td")

names = []
for td in tds:
    if len(td.find_all("a")) == 0:
        continue
    names.append(td.get_text(strip=True)) # 통화면 name array에 넣기

prices = []
for td in tds:
    if "class" in td.attrs:
        if "sale" in td.attrs["class"]:
            prices.append(td.get_text(strip=True))

print(names)
print(prices)

name = []
for td in soup.select("td.tit"):
    name.append(td.get_text(strip=True))

price = []
for td in soup.select("td.sale"):
    price.append(td.get_text(strip=True))

print(name)
print(price)