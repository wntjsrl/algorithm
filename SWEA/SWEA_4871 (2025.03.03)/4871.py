# SWEA 4871 그래프 경로 (2025.03.03)
def dfs(V, S, G):
    visited = [False] * (V + 1)
    stack = [None] * V
    top = -1
    while True:
        visited[S] = True
        for w in adj_list[S]:
            # 방문하지 않은 구간
            if visited[w] is False:
                top += 1
                stack[top] = S
                S = w
                break # for w in adj_list[S]
        else:
            # 현재 노드가 도착 노드일 때
            if S == G:
                return 1
            # stack이 비지 않았을 때
            if top != -1:
                top -= 1
                S = stack[top + 1]
            # stack이 비었을 때
            else:
                break # for w in adj_list[S]
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        v, w = map(int, input().split())
        adj_list[v].append(w)
    S, G = map(int, input().split())
    print(f"#{tc} {dfs(V, S, G)}")
