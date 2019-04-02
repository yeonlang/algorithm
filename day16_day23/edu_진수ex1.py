indata = ['0','F','9','7','A','3']
judge = ['A','B','C','D','E','F']

data = [0]*(len(indata)*4)
now = 0
for i in range(len(indata)):

    if indata[i] in judge:
        temp = 10 + judge.index(indata[i])
        for j in range(3,-1,-1):
            data[now] = 1 if temp & 1<<j else 0
            now+=1

    else :
        temp = int(indata[i])
        for j in range(3,-1,-1):
            data[now] = 1 if temp & 1<<j else 0
            now+=1

print(data)

t = 0
for i in range(len(data)):
    t = t*2 + int(data[i])
    if (i+1)%7 == 0:
        print(t)
        t = 0

if (i+1)%7 != 0:
    print(t)