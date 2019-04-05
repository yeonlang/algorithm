# def sol(c,lst,idx,cnt,cntsum,s,D):
#     global select
#     if cnt>K or c>M: return
#
#     if cntsum>D[0]:
#         D[0] = cntsum
#         select = s
#
#     for i in range(idx,len(lst)):
#         sol(c+1,lst,i+1,cnt+lst[i],cntsum+lst[i]**2,s,D)


def sol(c,idx):
    if c>N: return

    print(result)

    for i in range(idx,N):
        result.append(i)
        sol(c+1,i+1)
        result.pop()

N = 3
result = []
sol(0,0)
