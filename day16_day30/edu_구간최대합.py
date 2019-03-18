data = [5,1,-4,2,-1,-5,-2,8,-3,6]
RangeSum =[0]*len(data)
for now in range(len(data)):
    RangeSum[now] = max(RangeSum[now-1]+data[now],data[now])

result = max(RangeSum)
print(result)
i = RangeSum.index(result)
last = i
while data[i] != RangeSum[i]:
    i-=1
for j in range(i,last+1):
    print(data[j], end=" ")

                        