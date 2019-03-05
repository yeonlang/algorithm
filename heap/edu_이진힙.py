import sys
sys.stdin = open("이진힙.txt","r")

def insert(num):
    while num != 1:
        if heap[num] < heap[num//2]:
            heap[num//2], heap[num] = heap[num], heap[num//2]
            num = num//2
        else:
            break

for tc in range(int(input())):
    n = int(input())
    heap = [0] * (n+1)
    now = 0
    result = 0

    for i in map(int,input().split()):
        now += 1
        heap[now] = i
        insert(now)

    while now != 1:
        now = now // 2
        result += heap[now]


    print("#{} {}".format(tc+1,result))





