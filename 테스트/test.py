
# 부분집합
def subset(c,idx):
    print(choice)
    print(s-choice)

    if c==N:
        return

    for i in range(idx,N):
        choice.add(i)
        subset(c+1,i+1)
        choice.remove(i)

N = 5
s = set([0,1,2,3,4])
choice = set()
subset(0,0)