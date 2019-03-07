a=[1,2,3]
tree = [1 if i and i%2 == 0 else 0 for i in range(2**(len(a)+1))]

l = len(tree)
n=len(a)
choice =2

for start in range(2**(len(a)),2**(len(a)+1)):
    now = 0
    result = []

    while start != 1:
        if tree[start] == 1:
            result.append(a[now])
        now+=1
        start=start//2

    if len(result) == choice:
        print(result)
