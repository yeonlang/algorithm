import sys
sys.stdin = open("최종평가.txt")

def GCD(p, q):
    if not q:
        return p
    elif p < q :
        return GCD(q, p)
    else :
        return GCD(q,p%q)

for tc in range(int(input())):
    N, L, K = map(int,input().split())
    data = [0]
    for _ in range(L):
        y,x = map(int,input().split())
        data.append((y,x))
    INF1 = 9999
    INF2 = 8888
    A = [0]*(2*L+1)
    visited = [0]*(L+1)
    for i in range(1,L+1):
        visited[i] = 1
        dic = dict()
        for j in range(1,L+1):
            if not visited[j]:
                if not data[i][1]-data[j][1]:
                    if data[i][0] > data[j][0]:
                        temp = INF1
                    else:
                        temp = -INF1
                elif not data[i][0]-data[j][0]:
                    if data[i][1] > data[j][1]:
                        temp = INF2
                    else:
                        temp = -INF2
                else:
                    t1 = GCD(abs(data[j][0]-data[i][0]),abs(data[j][1] - data[i][1]))
                    temp = ((data[j][0]-data[i][0])/t1,(data[j][1] - data[i][1])/t1)
                try:
                    dic[temp].append(j)
                except KeyError:
                    dic[temp] = [j]

        cnt = len(dic)
        A[i] = cnt
        visited[i] = 0

    print("#{} {}".format(tc+1, sum(A)),end = " ")
    B = [0]*(2*L+1)
    C = [0]*(L+1)
    for i in range(1,L+1):
        for j in range(1,L+1):
            A[j] = (A[j]*K + j)%L +1
            A[L+j] = (A[j]*j + K)%L +1
        A.sort()
        B[0] = 1
        for j in range(1,2*L+1):
            B[j] = (B[j-1]*A[j]+j)%L + 1
        C[i] = B[2*L]
    print(sum(C))



