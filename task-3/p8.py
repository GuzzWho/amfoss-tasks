ai = list(map(int,input("").split()))
n=ai[0]
m=ai[1]
magic = []
normal = []
for num in range(m):
    sumtin = input("").split()
    for i in sumtin:
        if sumtin.index(i) == 0:
            magic.append(i)
        elif sumtin.index(i) == 1:
            normal.append(i)
spell = input("").split()
for x in range(n):
    index = 0
    for i in magic:
        if spell[x] == i:
            if len(spell[x])==len(normal[index]):
                spell[x] = i
            elif len(spell[x])>len(normal[index]):
                spell[x] = normal[index]
            else:
                spell[x] = i
        index += 1
for i in spell:
    print(i,end=" ")