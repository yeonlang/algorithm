import sys
sys.stdin = open('2309.txt', 'r')

def combinations(iterable, r):
    arr = sorted(iterable)
    nxt=0

    last=len(arr)-1
    comb = []

    while arr[last-r+1:] != comb:
        if len(comb) == r :
            if sum(comb) == 100:
                return comb
            check=comb.pop()
            n = 1
            while check == arr[-n]:
                n+=1
                check = comb.pop()
                nxt=arr.index(check)+1
        comb.append(arr[nxt])
        nxt=nxt+1

    return False

lst=[ int(input()) for _ in range(9)]

print(*combinations(lst, 7), sep='\n')





