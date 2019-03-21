import sys
sys.stdin = open("화물도크.txt")

for tc in range(int(input())):
    data = []
    for i in range(int(input())):
        data.append(tuple(map(int,input().split())))
    data.sort(key = lambda x: x[1])
    print(data)
    cnt = 1
    preend = data[0][1]
    for start,end in data:
        if start < preend:
            continue

        cnt+=1
        preend = end

    print("#{} {}".format(tc+1,cnt))
