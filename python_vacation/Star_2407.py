# 2407 유정은

scores = input("점수 입력 : ")
li = []
sl = [0,0,0,0,0]

li += scores.split(' ')

li = [int (i) for i in li]

for i in range(len(li)):
    if li[i] >= 90:
        sl[0] += 1
    elif li[i] >= 80:
        sl[1] += 1
    elif li[i] >= 70:
        sl[2] += 1
    elif li[i] >= 60:
        sl[3] += 1
    else: sl[4] += 1

print("90점 이상 : \t", "*"*sl[0])
print("80점 대 : \t", "*"*sl[1])
print("70점 대 : \t", "*"*sl[2])
print("60점 대 : \t", "*"*sl[3])
print("60점 미만 : \t", "*"*sl[4])
print("최고점수 :",max(li))
print("최저점수 :",min(li))
