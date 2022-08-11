# 2407 유정은

def isPrimeNumber(num):
    li = []
    count = 0
    for j in range(2, num+1):
        for i in range(2, j):
            count = 0
            if j % i == 0:
                count = 1
                break
        if count == 0:
            li += [j]

    print("소수: ", end='')
    for i in range(len(li)):
        print(li[i], end=' ')

    print()

    print("1 ~ {}까지의 소수의 갯수 : ".format(num), end='')
    print(len(li))


print("1 ~ N까지의 소수와 그 갯수를 구하는 프로그램")
num = int(input("N 입력 : "))
isPrimeNumber(num)
