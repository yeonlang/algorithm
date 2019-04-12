import sys
sys.stdin = open("차량정비소.txt")

class People:
    def __init__(self,id,time):
        self.id = id
        self.time = time
        self.TA = -1
        self.TB = -1

for tc in range(int(input())):
    N, M, P, A, B = map(int,input().split())
    waitA = []
    TableA = [0]*N
    waitB = []
    TableB = [0]*M
    SA = list(map(int,input().split()))
    SB = list(map(int,input().split()))
    finish = []
    data = list(map(int,input().split()))
    for i in range(P):
        data[i] = People(i+1,data[i])

    time = 0
    while True:
        if len(finish) == P:
            break

        i = 0
        while i<len(data):
            people = data[i]
            if time>=people.time:
                waitA.append(data.pop(i))
                continue
            i += 1

        for i in range(N):
            if TableA[i]:
                TableA[i].TA -= 1
                if not TableA[i].TA:
                    people = TableA[i]
                    people.ET = time
                    waitB.append(people)
                    TableA[i] = 0

        for j in range(M):
            if TableB[j]:
                TableB[j].TB -= 1
                if not TableB[j].TB:
                    finish.append(TableB[j])
                    TableB[j] = 0


        waitA.sort(key = lambda x:x.id)
        for i in range(N):
            if not TableA[i] and waitA:
                people = waitA.pop(0)
                people.TA = SA[i]
                people.s1 = i+1
                TableA[i] = people


        waitB.sort(key=lambda x:(x.ET,x.s1))
        for j in range(M):
            if not TableB[j] and waitB:
                people = waitB.pop(0)
                people.TB = SB[j]
                people.s2 = j+1
                TableB[j] = people

        time += 1

    ans = 0
    for people in finish:
        if people.s1 == A and people.s2 == B:
            ans+=people.id

    if not ans:
        print("#{} {}".format(tc+1,-1))
    else:
        print("#{} {}".format(tc+1,ans))



#접수창구의 우선순위
# ① 여러 고객이 기다리고 있는 경우 고객번호가 낮은 순서대로 우선 접수한다.
# ② 빈 창구가 여러 곳인 경우 접수 창구번호가 작은 곳으로 간다.

#정비 창구의 우선순위
# ① 먼저 기다리는 고객이 우선한다.
# ② 두 명 이상의 고객들이 접수 창구에서 동시에 접수를 완료하고 정비 창구로 이동한 경우, 이용했던 접수 창구번호가 작은 고객이 우선한다.
# ③ 빈 창구가 여러 곳인 경우 정비 창구번호가 작은 곳으로 간다.
#1 3
#2 7
#3 2
#4 22
#5 18
#6 15
#7 -1
#8 259
#9 100
#10 164
