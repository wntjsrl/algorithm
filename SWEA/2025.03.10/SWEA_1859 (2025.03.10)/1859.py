# SWEA 1859 백만 장자 프로젝트 (2025.03.10)

# import sys

# sys.stdin = open("1859_input.txt", "r")
# sys.stdout = open("1859_my_output.txt", "w")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    profit = max_price = 0
    # 뒤에서부터 가격 확인
    for price in reversed(arr):
        # 현재 주식이 가장 큰 주식보다 클 때
        if price > max_price:
            # 가장 큰 주식 변수에 현재 주식 가격으로 초기화
            max_price = price
        # 현재 주식이 가장 큰 주식보다 작을 때
        else:
            # 이익에 차익만큼 더하기
            profit += max_price - price
    print(f"#{tc} {profit}")
