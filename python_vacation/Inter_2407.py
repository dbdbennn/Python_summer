# 2407 유정은

def intersect(s1,s2):
    func_li = list()

    for i in s1:
        for j in s2:
            if i in j and i not in func_li:
                func_li.append(j)

    func_li.sort()
    return func_li
        
li = list()
s1 = (input("첫 번째 문자열 입력: "))
s2 = (input("두 번째 문자열 입력: "))
li = intersect(s1,s2) # 반환 받음
print(li)