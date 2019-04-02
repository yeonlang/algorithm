def insertionsort(num):
    i=0
    while i != len(result):
        if num<result[i]:
            result.insert(i,num)
            return
        i+=1
    result.append(num)

data = [1,9,3,6,7,0,4,9,5,5]

result = []
result.append(data.pop(0))

while data:
    insertionsort(data.pop(0))

print(data)
print(result)


