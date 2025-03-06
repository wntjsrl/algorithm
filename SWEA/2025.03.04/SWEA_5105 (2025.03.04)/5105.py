# SWEA 5105 미로의 거리 (2025.03.04)
# 시작점 찾는 메서드
def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == "2":
                return i, j

# bfs 메서드
def bfs(i, j):
    visited = [[0] * N for _ in range(N)]
    queue = [None] * (N * N)
    front = rear = -1
    # 시작점 인큐
    rear += 1
    queue[rear] = [i, j]
    visited[i][j] = 1
    # queue가 빌 때까지
    while front != rear:
        # 디큐
        front += 1
        i, j = queue[front]
        # 목적지에 도착하면 1 반환
        if maze[i][j] == "3":
            return visited[i][j] - 2
        # 상하좌우 순서로 델타 함수 적용
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            # 인덱스 넘어가지 않고, 벽이 아니고(1이 아니고), 방문하지 않았을 때
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != "1" and visited[ni][nj] == 0:
                # 인큐
                rear += 1
                queue[rear] = [ni, nj]
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = list(input() for _ in range(N))
    # 시작점 찾기
    sti, stj = find_start()
    print(f"#{tc} {bfs(sti, stj)}")
