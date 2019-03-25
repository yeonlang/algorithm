def search(T):
    global result1
    if 0<T<=n:
        search(T*2)
        result1 += tree[T]+' '
        search(T*2+1)


def search2(T):
    global result2
    if 0<T<=n:
        search2(T*2)
        search2(T*2+1)
        result2 += tree[T]+' '

def search3(T):
    global result3
    if 0<T<=n:
        result3 += tree[T]+' '
        search3(T*2)
        search3(T*2+1)

for tc in range(1):
    n = 7
    tree = [0]*(n+1)

    result1 = ''
    result2 = ''
    result3 = ''

    tree = [0]+[str(i) for i in range(1, n+1)]

    search(1)
    search2(1)
    search3(1)
    print("#{} {}".format(1, result1))
    print("#{} {}".format(2, result2))
    print("#{} {}".format(3, result3))