import sys
sys.stdin = open("최대상금.txt")

for tc in range(int(input())):
    data, K = input().split()
    K = int(K)
    N = len(data)
    now = set(list(data))
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1, N):
                    s[i], s[j] = s[j], s[i]
                    nxt.add("".join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now
    print("#{} {}".format(tc+1,max(map(int, now))))



    # 1 321
    # 2 7732
    # 3 857147
    # 4 87664
    # 5 88832
    # 6 777770
    # 7 966354
    # 8 954311
    # 9 332211
    # 10 987645
