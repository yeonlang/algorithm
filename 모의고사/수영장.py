import sys
sys.stdin = open("수영장.txt")

def BTK(now):
    global cnt,minpay

    if now>11:
        if cnt<minpay:
            minpay = cnt
        return

    for i,time in enumerate([3,1,1]):
        if i == 0:
            cnt+=trimon
            BTK(now+time)
            cnt-=trimon
        elif i == 1:
            cnt+=mon
            BTK(now+time)
            cnt-=mon
        else:
            temp = day*data[now]
            cnt += temp
            BTK(now+time)
            cnt -= temp

for tc in range(int(input())):
    day, mon, trimon, minpay = map(int,input().split())
    data = list(map(int,input().split()))

    cnt = 0
    BTK(0)
    print("#{} {}".format(tc+1,minpay))

