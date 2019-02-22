def paper(n):
    if n<3:
        return 2*n-1
    else:
        return paper(n-1) + paper(n-2) * 2


for tc in range(int(input())):
    N = int(input())
    n = N // 10
    print(f'#{tc+1} {paper(n)}')