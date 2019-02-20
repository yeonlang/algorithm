def dfs(start):
    global dic
    stack=[start]
    visited=set()

    while stack:
        now=stack.pop()
        if not now in visited:
           print(now)
        visited.add(now)
        c=list(dic[now] - visited)
        c.sort(reverse=True)
        stack+=c

lst=[1,2, 1,3, 2,4, 2,5, 4,6, 5,6, 6,7, 3,7]

dic={ i:set() for i in range(1,max(lst)+1)}
for i in range(len(lst)//2):
    dic[lst[2*i]].add(lst[2*i+1])
    dic[lst[2*i+1]].add(lst[2*i])

dfs(3)
