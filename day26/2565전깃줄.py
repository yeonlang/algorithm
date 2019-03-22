import sys
sys.stdin = open("2565전깃줄.txt")

def update(a,b):
    where = base +a -1
    tree[where] = b
    where >>= 1

    while where:
        tree[where] = tree[where*2]+tree[where*2+1]
        where >>=1

N = int(input())
data = [0]*(11)
for i in range(N):
    idx, value = map(int,input().split())
    data[idx] = value
print(data)
base = 1
while base <= N:
    base <<= 1
tree = [0]*(base*2)

for now in range(base, N + base):
    idx = now-base+1
    if 0<=idx<N and data[idx]>


