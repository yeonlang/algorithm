import sys
sys.stdin = open("소방차.txt","r")

def sol(now,now_sum):
    global pumps, min_sum

    if now>=f:
        if now_sum < min_sum:
            min_sum = now_sum
        return

    if now_sum>min_sum:
        return

    for i in range(f):
        for j in range(p):
            if not visitedP[j] and not visitedF[i]:
                now_sum += abs(cars[i]-pumps[j])
                visitedP[j],visitedF[i] = 1,1
                sol(now+1,now_sum)
                visitedP[j],visitedF[i] = 0,0
                now_sum -= abs(cars[i]-pumps[j])


p, f = map(int,input().split())
pumps = list(map(int,input().split()))
cars = list(map(int,input().split()))
visitedP = [0]*p
visitedF = [0]*f
min_sum=987654321

sol(0,0)

print(min_sum)
