# SWEA 길찾기 (2025.03.03)
def dfs(S, G):
    visited = [False] * 100
    stack = [None] * 100
    top = -1
    # 시작 노드 push
    top += 1
    stack[top] = S
    # stack이 빌 때까지 반복
    while top != -1:
        # pop
        top -= 1
        S = stack[top + 1]
        visited[S] = True
        # 도착 노드에 도달했을 때
        if S == G:
            return 1
        for w in adj_list[S]:
            # 방문하지 않은 노드일 때
            if not visited[w]:
                # 해당 노드 push
                top += 1
                stack[top] = w
    return 0

for _ in range(1, 11):
    test_case, E = map(int, input().split())
    graph = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]
    for i in range(E):
        adj_list[graph[i*2]].append(graph[i*2 + 1])
    print(f"#{test_case} {dfs(0, 99)}")
