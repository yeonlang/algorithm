def BTK(choice):
    global result
    if choice==len(data):
        print(result)
        return

    for i in range(len(data)):
        if not visited[i]:
            visited[i]=1
            result[choice]=data[i]
            BTK(choice+1)
            result[choice]=0
            visited[i]=0

data=[1,2,3,4,5]
visited=[0]*len(data)
result=[0]*len(data)
BTK(0)