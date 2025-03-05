# SWEA 5174 subtree (2025.03.05)
# global count 사용하는 경우

# 서브트리 노드 갯수 구하는 함수
def count_subtree_nodes(n):
    global count
    # 노드가 존재할 경우
    if n:
        count += 1
        count_subtree_nodes(left_ch[n])
        count_subtree_nodes(right_ch[n])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    # 마지막 노드 번호
    V = E + 1
    left_ch = [None] * (V + 1)
    right_ch = [None] * (V + 1)
    par = [None] * (V + 1)
    for i in range(0, E * 2, 2):
        p, c = arr[i], arr[i + 1]
        par[c] = p
        if left_ch[p] is None:
            left_ch[p] = c
        else:
            right_ch[p] = c
    count = 0
    count_subtree_nodes(N)
    print(f"#{tc} {count}")

# # global count를 사용하지 않는 경우
#
# # 서브트리 노드 갯수 구하는 함수
# def count_subtree_nodes(n):
#     # 노드가 존재하지 않을 경우
#     if n is None:
#         return 0
#     else:
#         # 왼쪽 서브트리의 정점 수
#         l = count_subtree_nodes(left_ch[n])
#         # 오른쪽 서브트리의 정점 수
#         r = count_subtree_nodes(right_ch[n])
#         return l + r + 1
#
# T = int(input())
# for tc in range(1, T + 1):
#     E, N = map(int, input().split())
#     arr = list(map(int, input().split()))
#     # 마지막 노드 번호
#     V = E + 1
#     left_ch = [None] * (V + 1)
#     right_ch = [None] * (V + 1)
#     par = [None] * (V + 1)
#     for i in range(0, E * 2, 2):
#         p, c = arr[i], arr[i + 1]
#         par[c] = p
#         if left_ch[p] is None:
#             left_ch[p] = c
#         else:
#             right_ch[p] = c
#     print(f"#{tc} {count_subtree_nodes(N)}")
