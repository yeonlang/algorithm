import sys
sys.stdin = open("수영장.txt")

def BTK(now,cnt):
    global minpay

    if now>11:
        if cnt<minpay:
            minpay = cnt
        return

    for i,time in enumerate([3,1,1]):
        if i == 0: BTK(now+time,cnt+trimon)
        elif i == 1: BTK(now+time,cnt+mon)
        else: BTK(now+time,cnt+day*data[now])

for tc in range(int(input())):
    day, mon, trimon, minpay = map(int,input().split())
    data = list(map(int,input().split()))

    BTK(0,0)
    print("#{} {}".format(tc+1,minpay))

