# SWEA 파스칼 삼각형 (2025.03.02)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # arr 요소 모두를 1로 초기화
    arr = [[1] * (i + 1) for i in range(N)]
    # 3번째 줄부터 계산
    for i in range(2, N):
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    print(f"#{tc}")
    for item in arr:
        print(*item)
