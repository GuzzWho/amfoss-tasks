ai = list(map(int,input("").split()))
n=ai[0]
m=ai[1]
if n%2==0:
    count2 = int(n/2)
    count1=0
else:
    count2 = int(n/2)
    count1 =1
flag=1
while count2!=-1 :
    if(count1+count2)%m==0:
        print(count1+count2)
        flag = 0
        break
    else:
        count1 += 2
        count2 -= 1
if flag:
    print(-1)
