a=['a','l','g','o','r','i','t','h','m']
n=len(a)
m=n//2

for i in range(1,m+1):
    a[m+i], a[m-i] = a[m-i], a[m+i]


print("".join(a))
