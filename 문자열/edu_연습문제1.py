a=['a','l','g','o','r','i','t','h','m']
n=len(a)
m=n//2
if n&1:
    for i in range(m):
        a[m + i +1], a[m - i + 1] = a[m - i + 1], a[m + i +1]
else:
    m=n//2

print(a)
