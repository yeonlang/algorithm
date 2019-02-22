def test():
    global c, lst
    a = c
    lst+=[4]
    print(lst)

lst=[1,2,3]
c=4
test()
