def Power1(a,b):
    if b==0: return 1
    elif b == 1 : return a
    elif b&1 : return a*Power1(a,b-1)
    else :
        temp = Power1(a,b//2)
        return temp*temp

def Power2(a,b):
    ans = 1
    while b>0:
        if b&1 : ans*=a
        a = a*a
        b//=2
    return ans

print(Power1(3,2))
print(Power2(3,2))