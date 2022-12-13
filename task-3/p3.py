import math
ai = list(map(int,input("").split()))
n=ai[0]
m=ai[1]
if m%n == 0:
    num = m/n
    prime = []
    while num % 2 == 0:
        prime.append(2)
        num = num / 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            prime.append(i)
            num = num / i
    if num > 2:
        prime.append(num)
    flag = 1
    for x in set(prime):
        if x not in {2, 3}:
            print(-1)
            flag = 0
            break
    if flag:
       print(len(prime))
else:
    print(-1)