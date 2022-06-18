s = "apple"
print(s)

print(s.find("e")) # 4

arr = s.split("p") 
print(arr) # ['a', '', 'le']

s1 = "제 생일은 10월 입니다."
# print(s1.find("생일은 ")) # 2
# pos = s1.find("생일은 ")
# pos += 4
# print(s1[pos:pos+1]) # 9
  
# print(s1[6:7]) # 9

arr = s1.split("생일은 ")
s1 = arr[1]
print(s1.split("월")[0])


s2 = "제 생일은 10월 입니다."
bd=s2.split("생일은 ")[1].split("월")[0]
print(bd)