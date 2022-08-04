s = input("영문자 입력 : ")
li = []
for i in range(len(s)):
    li += s[i]

li.reverse()

print("거꾸로 출력 : ",end='')
for i in range(len(s)):
    print(li[i], end='')