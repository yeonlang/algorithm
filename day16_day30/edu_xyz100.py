def n_recu():
    result = set()
    for i in range(1,101):
        for j in range(1,101):
            for k in range(1,101):
                if i+j+k == 100:
                    data = [i,j,k]
                    data.sort()
                    result.add(tuple(data))
    print(len(result))

def recu(x=1,y=1,z=1):
    global result
    visited.append((x,y,z))

    if visited.count((x,y,z)) > 1:
        return

    if x+y+z == 80:
        temp = [x,y,z]
        temp.sort()
        result.add(tuple(temp))
        return

    recu(x+1,y,z)
    recu(x,y+1,z)
    recu(x,y,z+1)

result = set()
visited = []
recu()
print(len(result))



