import requests as req

res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")

# print(res.text)
html = res.text
#print(html)

# pos = html.find("미국 USD")
# print(pos)

pos1 = '<span class="value">'
pos2 = "</span>"
s = html.split(pos1)[1].split(pos2)[0]
print(s)