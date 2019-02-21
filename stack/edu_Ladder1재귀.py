import sys

sys.stdin = open("1210.txt", "r")


def dfs(start):
    y, x = start[0],start[1]
    visited[y][x] = 1

    for nxt in range(3):
        nx = x + dx[nxt]
        ny = y + dy[nxt]
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and lst[ny][nx]:
            if ny == 0:
                return nx
            return dfs((ny,nx))




for tc in range(1):

    z = input()
    del z

    lst = []
    lst.append(list(map(int, input().split())))
    n = len(lst[0])
    for i in range(n - 1):
        if i == n - 2:
            temp = list(map(int, input().split()))
            end = temp.index(2)
            lst.append(temp)
            del temp
            break
        lst.append(list(map(int, input().split())))

    visited = [[0] * n for i in range(n)]
    # 우, 좌, 상
    dx = [1, -1, 0]
    dy = [0, 0, -1]

    print(f"#{tc+1} {dfs((n - 1, end))}")
