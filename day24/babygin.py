import sys
sys.stdin = open("babygin.txt")

def read(a,b,c):
    if a == b-1 == c-2:
        return True
    if a == b == c:
        return True
    return False

for tc in range(int(input())):
    data = list(map(int,input().split()))
    cnt = [0,0,0,0,0,0]
    s = set()
    for n1 in range(6):
        for n2 in range(6):
            for n3 in range(6):
                for n4 in range(6):
                    for n5 in range(6):
                        for n6 in range(6):
                            cnt = [0, 0, 0, 0, 0, 0]
                            cnt[n1]+=1; cnt[n2]+=1; cnt[n3]+=1; cnt[n4]+=1; cnt[n5]+=1; cnt[n6]+=1
                            if 0 in cnt:
                                continue
                            if read(data[n1],data[n2],data[n3]) and read(data[n4],data[n5],data[n6]):
                                s.add((data[n1],data[n2],data[n3],data[n4],data[n5],data[n6]))
    for a,b,c,d,e,f in s:
        print('{}, {}, {}, {}, {}, {} 은 babyjin입니다.'.format(a, b, c, d, e, f))