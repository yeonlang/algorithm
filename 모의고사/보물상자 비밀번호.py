import sys
sys.stdin = open("보물상자 비밀번호.txt")

def trans(s):
    if ord('0')<=ord(s)<=ord('9'):
        return int(s)
    else:
        return ord(s)-55

def turn():
    temp = data[N-1]
    for i in range(N-1,0,-1):
        data[i] = data[i-1]
    data[0] = temp

for tc in range(int(input())):
    N,K = map(int,input().split())
    U = N//4
    data = list(map(trans,input()))
    result = set()
    for i in range(N+1):
        t = 0
        while t<4*U:
            result.add(tuple(data[t:t+U]))
            t += U
        turn()
    ans = []
    for i in result:
        t = len(i)-1
        cnt = 0
        for j in i:
            cnt+= j*(16**t)
            t-=1
        ans.append(cnt)
    ans.sort(reverse=True)
    print("#{} {}".format(tc+1,ans[K-1]))

