import sys
sys.stdin = open("예산관리.txt","r")

def BTK(now):
    global my_min

    if (goal - now) < my_min:
        my_min = goal - now

    for nxt in range(n):
        if now + dir[nxt]> goal:
            continue

        if not visited[nxt]:
            now+=dir[nxt]
            visited[nxt]=1
            BTK(now)
            visited[nxt]=0
            now -= dir[nxt]

goal = int(input())
n = int(input())
my_min=goal
now = 0
dir = [ num for num in map(int,input().split())]
visited = [0] * n

BTK(now)
print(goal-my_min)

