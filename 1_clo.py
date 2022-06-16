s = "apple"
print(s)

print(s.find("e")) # 4

arr = s.split("p") 
print(arr) # ['a', '', 'le']

s1 = "제 생일은 9월 입니다."
print(s1.find("생일은 ")) # 2
pos = s1.find("생일은 ")
pos += 4
print(s1[pos:pos+1]) # 9

print(s1[6:7]) # 9
