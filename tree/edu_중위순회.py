import sys
sys.stdin = open("중위순회.txt","r")

def search(T):
    global result
    if 0<T<=n:
        search(T*2)
        result+=tree[T]
        search(T*2+1)


for tc in range(10):
    n = int(input())
    tree = [0] * (n+1)
    result = ''
    for i in range(n):
        data = list(input().split())
        tree[int(data[0])] = data[1]
    search(1)
    print("#{} {}".format(tc+1,result))
