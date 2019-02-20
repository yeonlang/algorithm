def GetSome(here):
    global ans
    if here == howmany:
        ans +=1
        return None
    if here > howmany:
        return None
    GetSome(here+1)
    GetSome(here+2)

def stair(n):
    if n < 3:
        return n
    return stair(n-1) + stair(n-2)

ans = 0
howmany = int(input())
GetSome(0)
print(ans)


