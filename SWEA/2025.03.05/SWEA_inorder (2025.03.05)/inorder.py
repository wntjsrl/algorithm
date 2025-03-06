# SWEA 중위순회 (2025.03.05)

# 중위순회하는 함수
def in_order(n):
    # 최대 정점 번호 이내인 경우 유효
    if n <= N:
        # 왼쪽 자식
        in_order(n * 2)
        print(tree[n], end="")
        # 오른쪽 자식
        in_order(n*2 + 1)

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    for _ in range(N):
        v, c, *child = input().split()
        # 완전 이진 트리
        tree[int(v)] = c
    print(f"#{tc}", end=" ")
    # 루트부터 중위순회
    in_order(1)
    print()
