def Power(a,b):
    t = 1
    for i in range(1,b+1):
        t *= a
    return t

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

print(Power(4,5))
print(Power2(4,5))
print(Power2(4,5))