class Node():
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist

def dfs2(N):
    global max_dist
    visit.append(N.node)
    stack.append(N.node)
    if N.dist > max_dist:
        max_dist = N.dist
    while stack:
        node = stack.pop()
        for n in graph[node]:
            if n not in visit:
                d = N.dist + 1
                dfs2(Node(n,d))

for t in range(int(input())):
    n, m = list(map(int, input().split()))
    graph = dict()
    result = []

    # 그래프 생성
    for i in range(1,n+1):
        graph[str(i)] = []

    # 그래프 간선정보 초기화
    for _ in range(m):
        i, j = input().split()
        graph[i].append(j)
        graph[j].append(i)

    # 모든 노드에서 최장경로를 조사한다.
    for i in graph.keys():
        visit = []
        stack = []
        max_dist = 0
        dfs2(Node(i, 1))
        result .append(max_dist)

    print("#{} {}".format(t+1, max(result))) # 최장경로값 출력