def getsum(start,index,nowsum):
    global indata
    road.append(start)
    nowsum+=start
    if sum(road) == goal:
        print(road)
        print(nowsum)
        # result=road[:]
        return
    if sum(road) > goal:
        return

    for x in range(index+1,len(data)):
        if not indata[x] :
            indata[x] = 1
            getsum(data[x],x,nowsum)
            road.pop()
            indata[x] = 0


data=[1,2,3,4,5,6,7,8,9,10]
indata=[0]*(len(data)+1)
goal=10
road=[]
for i in range(len(data)):
    getsum(data[i],i,0)
    road.pop()

