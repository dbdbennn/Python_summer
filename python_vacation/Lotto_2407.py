import random
def func_lotto():
    li = list()

    for i in range(6):
        n = random.randint(1,20)
        while n in li:
            n = random.randint(1,20)
        li.append(n)

    return li

for i in range(10):
    li = func_lotto()
    li.sort()

    print("당첨번호 : ", end='')
    for i in range(len(li)):
        print(li[i], end=' ')
    
    print()