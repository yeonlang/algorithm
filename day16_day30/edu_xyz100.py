result = set()
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            if i+j+k == 100:
                data = [i,j,k]
                data.sort()
                result.add(tuple(data))
print(len(result))
