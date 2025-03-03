# SWEA 4869 종이붙이기 (2025.03.03)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 1의 자리로 나눠주기
    n = N // 10
    # dp 배열 초기화
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        # 점화식 f[n] = f[n - 1] + 2*f[n - 2]
        dp[i] = dp[i - 1] + 2*dp[i - 2]
    print(f"#{tc} {dp[n]}")
