# SWEA 5178 노드의 합 (2025.03.05)

# 지정한 노드의 값을 반환하는 함수
def find_tree_value(tree, N, L):
    for i in range(N, 1, -1):
        tree[i // 2] += tree[i]
    return tree[L]

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        v, w = map(int, input().split())
        tree[v] = w
    print(f"#{tc} {find_tree_value(tree, N, L)}")
