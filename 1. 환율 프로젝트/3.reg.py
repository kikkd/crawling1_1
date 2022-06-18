import re

# s = "hi"
# print(re.match(r"..",s))

# s = "hi"
# print(re.match(r"hi*",s))

# s = "hi111"
# print(re.match(r"hi+",s))

# s = "color"
# print(re.match(r"colou?r",s))

# s = "how are you?"
# print(re.match(r"how are you\?",s))

# A B C F
s = "이 영화는 A등급 입니다."
print(re.match(r"이 영화는 A등급 입니다.",s))

s = "이 영화는 A등급 입니다."
print(re.match(r"이 영화는 [ABC]등급 입니다.",s))

s = "이 영화는 A등급 입니다."
s = s.split("이 영화는 ")[1].split("등급 입니다.")[0]
print(s)
#print(re.match(r"이 영화는 [ABC]등급 입니다.",s))

s = "이 영화는 A등급 입니다."
print(re.findall(r"이 (..)는 ([ABC])등급 입니다.",s))