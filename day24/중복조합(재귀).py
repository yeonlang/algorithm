def BTK(n,r,choice=0,idx=0):
    if choice == r:
        print(result)
        return
    if idx>=n:
        return
    result[choice] = idx+1
    BTK(n,r,choice+1,idx)
    BTK(n,r,choice,idx+1)

n = 5
r = 3
result = [0]*r
BTK(5,3)

