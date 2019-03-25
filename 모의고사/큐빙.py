import sys
sys.stdin = open("큐빙.txt")

def turn(s,space,d):
        if d == '+':
            s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9] = s[7],s[4],s[1],s[8],s[5],s[2],s[9],s[6],s[3]
        if d == '-':
            s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9] = s[3],s[6],s[9],s[2],s[5],s[8],s[1],s[4],s[7]

        if space == 'U' and d == '+':
            B[7],B[8],B[9],R[1],R[4],R[7],F[3],F[2],F[1],L[9],L[6],L[3] = L[9],L[6],L[3],B[7],B[8],B[9],R[1],R[4],R[7],F[3],F[2],F[1]
        elif space=='U' and d == '-':
            B[7],B[8],B[9],R[1],R[4],R[7],F[3],F[2],F[1],L[9],L[6],L[3] = R[1],R[4],R[7],F[3],F[2],F[1],L[9],L[6],L[3],B[7],B[8],B[9]

        elif space == 'B' and d == '+':
            D[7],D[8],D[9],R[3],R[2],R[1],U[3],U[2],U[1],L[3],L[2],L[1] = L[3],L[2],L[1],D[7],D[8],D[9],R[3],R[2],R[1],U[3],U[2],U[1]
        elif space=='B' and d == '-':
            D[7],D[8],D[9],R[3],R[2],R[1],U[3],U[2],U[1],L[3],L[2],L[1] = R[3],R[2],R[1],U[3],U[2],U[1],L[3],L[2],L[1],D[7],D[8],D[9]

        elif space == 'F' and d == '+':
            U[7],U[8],U[9],R[7],R[8],R[9],D[3],D[2],D[1],L[7],L[8],L[9] = L[7],L[8],L[9],U[7],U[8],U[9],R[7],R[8],R[9],D[3],D[2],D[1]
        elif space=='F' and d == '-':
            U[7],U[8],U[9],R[7],R[8],R[9],D[3],D[2],D[1],L[7],L[8],L[9] = R[7],R[8],R[9],D[3],D[2],D[1],L[7],L[8],L[9],U[7],U[8],U[9]

        elif space == 'L' and d == '+':
            B[1],B[4],B[7],U[1],U[4],U[7],F[1],F[4],F[7],D[1],D[4],D[7] = D[1],D[4],D[7],B[1],B[4],B[7],U[1],U[4],U[7],F[1],F[4],F[7]
        elif space=='L' and d == '-':
            B[1],B[4],B[7],U[1],U[4],U[7],F[1],F[4],F[7],D[1],D[4],D[7] = U[1],U[4],U[7],F[1],F[4],F[7],D[1],D[4],D[7],B[1],B[4],B[7]

        elif space == 'R' and d == '+':
            B[9],B[6],B[3],D[9],D[6],D[3],F[9],F[6],F[3],U[9],U[6],U[3] = U[9],U[6],U[3],B[9],B[6],B[3],D[9],D[6],D[3],F[9],F[6],F[3]
        elif space=='R' and d == '-':
            B[9],B[6],B[3],D[9],D[6],D[3],F[9],F[6],F[3],U[9],U[6],U[3] = D[9],D[6],D[3],F[9],F[6],F[3],U[9],U[6],U[3],B[9],B[6],B[3]

        elif space == 'D' and d == '+':
            F[7],F[8],F[9],R[9],R[6],R[3],B[3],B[2],B[1],L[1],L[4],L[7] = L[1],L[4],L[7],F[7],F[8],F[9],R[9],R[6],R[3],B[3],B[2],B[1]
        elif space=='D' and d == '-':
            F[7],F[8],F[9],R[9],R[6],R[3],B[3],B[2],B[1],L[1],L[4],L[7] = R[9],R[6],R[3],B[3],B[2],B[1],L[1],L[4],L[7],F[7],F[8],F[9]


for tc in range(int(input())):
    U = [0,'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
    D = [0,'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
    F = [0,'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
    B = [0,'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    L = [0,'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']
    R = [0,'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

    N = int(input())
    data = []
    for i in input().split():
        s,d = i
        data.append((s,d))

    for i,j in data:
        if i == 'U': turn(U,'U',j)
        elif i=='B': turn(B,'B',j)
        elif i=='R': turn(R,'R',j)
        elif i=='F': turn(F,'F',j)
        elif i=='L': turn(L,'L',j)
        elif i=='D': turn(D,'D',j)

    for u in range(3):
        print("".join(U[3*u+1:3*u+4]))