import sys
sys.stdin = open('2606.txt', 'r')

def dfs(dic, start):
    visited = set()
    stack=[start]

    while stack:
        start=stack.pop()
        if start not in visited:
            visited.add(start)
            stack += dic[start] - visited

    return len(visited)-1

K=int(input())
dic={}

for _ in range(int(input())):
    node, nxt = map(int, input().split())

    if node in dic:
        dic[node].add(nxt)
        if nxt in dic:
            dic[nxt].add(node)
        else:
            dic[nxt] = set([node])
    else:
        dic[node] = set([nxt])
        dic[nxt] = set([node])

lst= list(dfs(dic,1))
print(len(lst)-1)






