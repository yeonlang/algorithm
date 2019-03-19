import sys
sys.stdin = open("암호코드스캔.txt","r")

C = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
C[3][1][1] = 0
C[2][2][1] = 1
C[1][2][2] = 2
C[4][1][1] = 3
C[1][3][2] = 4
C[2][3][1] = 5
C[1][1][4] = 6
C[3][1][2] = 7
C[2][1][3] = 8
C[1][1][2] = 9

A = ord('A')
nine, zero = ord('9'), ord('0')


def getHex(ch):
    t = ord(ch)
    return (t - A) + 10 if t > nine else t - zero


def scanner():
    read = [0] * 8
    ans = 0
    for i in range(N):
        j = M - 1
        while j >= 0:
            if D[i][j] != '0' and D[i - 1][j] == '0':
                val = getHex(D[i][j])
                idx, cnt = 7, 0
                while idx >= 0:
                    cnt2 = cnt3 = cnt4 = 0
                    while val & 1 == 0:
                        val >>= 1
                        cnt += 1
                        if cnt == 4:
                            j, cnt = j - 1, 0
                            val = getHex(D[i][j])

                    while val & 1:
                        cnt4, cnt = cnt4 + 1, cnt + 1
                        val >>= 1
                        if cnt == 4:
                            j, cnt = j - 1, 0
                            val = getHex(D[i][j])

                    while val & 1 == 0:
                        cnt3, cnt = cnt3 + 1, cnt + 1
                        val >>= 1
                        if cnt == 4:
                            j, cnt = j - 1, 0
                            val = getHex(D[i][j])

                    while val & 1:
                        cnt2, cnt = cnt2 + 1, cnt + 1
                        val >>= 1
                        if cnt == 4:
                            j, cnt = j - 1, 0
                            val = getHex(D[i][j])

                    MIN = min(min(cnt2, cnt3), cnt4)
                    cnt2, cnt3, cnt4 = cnt2 // MIN, cnt3 // MIN, cnt4 // MIN
                    read[idx] = C[cnt2][cnt3][cnt4]
                    idx = idx - 1

                a = read[0] + read[2] + read[4] + read[6]
                b = read[1] + read[3] + read[5] + read[7]
                if (a * 3 + b) % 10 == 0:
                    ans += (a + b)
            j -= 1
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    D = [list(input()) for _ in range(N)]
    print('#%d %d' % (tc, scanner()))