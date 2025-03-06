# SWEA 5177 이진 힙 (2025.03.05)

# 마지막 정점의 조상 노드의 값의 합을 구하는 함수
def an_sum(heap, last):
    an_sum = 0
    while last:
        last //= 2
        an_sum += heap[last]
    return an_sum

# 최소 힙에 노드 삽입
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    # 부모가 있고, 부모 > 자식 (최소 힙 조건 위반)
    while p != 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 부모의 부모
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N + 1)
    # 마지막 정점
    last = 0
    for i in range(N):
        enq(arr[i])
    print(f"#{tc} {an_sum(heap, last)}")
