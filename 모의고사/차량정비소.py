import sys
sys.stdin = open("차량정비소.txt")

for tc in range(int(input())):
    N1, N2, people, A, B = map(int,input().split())
    power1 = [0]*N1
    table1 = [0]*N1
    power2 = [0]*N2
    table2 = [0]*N2

    data = []
    for u,value in enumerate(map(int,input().split())):
        power1[u] = value
    for u,value in enumerate(map(int,input().split())):
        power2[u] = value
    for u,value in enumerate(map(int,input().split())):
        data.append((u+1,value))
    data.sort(key=lambda x:(x[1],x[0]))

    choice1 = []
    choice2 = []
    wait1 = []
    wait2 = []
    end = []

    time = 0
    while len(end) != people:
        for num in range(N1):
            if table1[num]:
                table1[num][0]-=1
                if table1[num][0] == 0:
                    wait2.append((table1[num][1],time,num))
                    table1[num] = 0
        if wait2:
            wait2.sort(key=lambda x:(x[1],x[2]))

        for num in range(N2):
            if table2[num]:
                table2[num][0]-=1
                if table2[num][0] == 0:
                    end.append(table2[num][1])
                    table2[num] = 0

        while data and data[0][1] == time:
            wait1.append(data.pop(0))
            wait1.sort(key=lambda x : x[0])

        while wait1:
            flag = True
            peoplenum,j = wait1.pop(0)
            for num in range(N1):
                if table1[num] == 0:
                    if num == A-1:
                        choice1.append(peoplenum)
                    table1[num] = [power1[num],peoplenum]
                    flag = False
                    break
            if flag:
                wait1.insert(0,(peoplenum,j))
                break

        while wait2:
            flag = True
            peoplenum,j,desk = wait2.pop(0)
            for num in range(N2):
                if table2[num] == 0:
                    if num == B-1 and peoplenum in choice1:
                        choice2.append(peoplenum)
                    table2[num] = [power2[num],peoplenum]
                    flag = False
                    break
            if flag:
                wait2.insert(0,(peoplenum,j,desk))
                break
        time+=1

    if choice2:
        print("#{} {}".format(tc+1,sum(choice2)))
    else :
        print("#{} {}".format(tc+1,-1))