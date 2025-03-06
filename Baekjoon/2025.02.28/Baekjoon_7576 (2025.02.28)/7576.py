# 백준 7576 토마토 (2025.02.28)
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = [[0, 0]] * (N * M)
rear = front = -1
max_v = 0
# 시작점 큐에 담기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            # 인큐
            rear += 1
            q[rear] = [i, j]
# BFS
while front != rear:
    # 디큐
    front += 1
    i, j = q[front]
    # 상하좌우 델타 함수 적용
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            # 인큐
            rear += 1
            q[rear] = [ni, nj]
            arr[ni][nj] = arr[i][j] + 1
            max_v = arr[ni][nj] - 1
# 토마토 자라기가 완료됐는지 확인
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            # for j
            break
        continue
    # for i
    break
else:
    print(max_v)
