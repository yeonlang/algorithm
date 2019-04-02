num=int(input())
lst = [ -1 for i in range(num)] 

for i in range(num):
    lst[i] = lst[i-1] + 1
    if (i+1) % 2 == 0:
        lst[i] = min([lst[i], lst[int(i/2)]+1])
    if (i+1) % 3 == 0:
        lst[i] = min([lst[i], lst[int(i/3)]+1])

print(lst[num-1])