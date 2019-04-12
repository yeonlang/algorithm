import sys
sys.stdin = open("리모컨.txt")

from collections import deque
def cal(now,num):
    if 0<=num<10:
        return int(str(now)+str(num))
    elif num == 10:
        return now+1
    elif num == 11:
        return now-1

def BFS():
    stack = deque([(100,0)])
    visited[0][100] = 1

    while stack:
        now,flag = stack.popleft()
        if visited[1][find] or visited[0][find]: return

        for x in dx:
            # 버튼을 눌러서 왔고 다시 버튼을 눌렀다.
            if flag and x<10:
                nxt = cal(now,x)
                nxtflag = 1

            # 버튼을 눌러서 오지 않았지만 버튼을 눌렀다.
            elif not flag and x<10:
                nxt = cal(0,x)
                nxtflag = 1

            # +,-를 눌렀다.
            else:
                nxt = cal(now,x)
                nxtflag = 0

            if 0<=nxt<=1000000 and not visited[nxtflag][nxt] :
                visited[nxtflag][nxt] = visited[flag][now]+1
                stack.append((nxt,nxtflag))

dx = set(i for i in range(12))
find = int(input())
N =int(input())

if N:
    B = set(map(int,input().split()))
else:
    B = set()

dx ^= B
judge = set(i for i in range(10))

visited = [[0]*1000001 for _ in range(2)]

if judge&dx:
    BFS()
    print(max(visited[0][find]-1,visited[1][find]-1))

else :
    print(abs(100-find))
