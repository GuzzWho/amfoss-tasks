n = int(input())
ord = []
abs = []
for num in range(n):
    sumtin = list(map(int,input("").split()))
    ord.append(sumtin[0])
    abs.append(sumtin[1])
count=0
for x in range(n):
    flag=0
    flag1=0
    flag2=0
    flag3=0
    for i in range(n):
      if x!=i:
        if abs[x]==abs[i]:
            if ord[x]<ord[i]:
                flag = 1
            else:
                flag1=1
    for i in range(n):
      if x != i:
        if ord[x]==ord[i]:
            if abs[x]>abs[i]:
                flag2=1
            else:
                flag3=1
    if flag and flag1 and flag2 and flag3:
        count += 1
print(count)
