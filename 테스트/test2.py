class T:
    def __init__(self,i):
        self.i = i

a = T(1)
b = T(2)
c = T(3)

lst = []
lst.append(a)
lst.append(b)
lst.append(c)



print(lst[1].i)