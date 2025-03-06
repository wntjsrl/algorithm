# SWEA 5176 이진탐색 (2025.03.05)

# global 쓰는 버전
# 중위순회하는 함수
def in_order(n):
    global cnt
    # 최대 정점 번호 이내인 경우 유효 (완전 이진 트리)
    if n <= N:
        # 왼쪽 자식
        in_order(n * 2)
        # 해당 노드에 1부터 N까지의 값 순서대로 저장
        tree[n] = cnt
        cnt += 1
        # 오른쪽 자식
        in_order(n*2 + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    in_order(1)
    print(f"#{tc} {tree[1]} {tree[N // 2]}")

# # global 안 쓰는 버전
# # 왼쪽에 위치한 조상의 순서 a
# def f(i, a):
#     # 완전 이진 트리
#     if i > N:
#         # 서브트리의 정점 0개
#         return 0
#     else:
#         # l 서브트리의 정점 갯수 리턴
#         l = f(i * 2, a)
#         tree[i] = l + a + 1
#         r = f(i*2 + 1, tree[i])
#         return l + r + 1
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     tree = [0] * (N + 1)
#     cnt = 1
#     f(1, 0)
#     print(f"#{tc} {tree[1]} {tree[N // 2]}")
