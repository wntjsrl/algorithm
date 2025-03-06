# SWEA 5186 이진수2 (2025.03.06)
# import sys

# sys.stdin = open("5186_input.txt", "r")
# sys.stdout = open("5186_my_output.txt", "w")
T = int(input())
for tc in range(1, T + 1):
    N = input()
    n = float(N)
    binary_str = ""
    for _ in range(12):
        n *= 2
        if n >= 1:
            binary_str += "1"
            n -= 1
        else:
            binary_str += "0"
        # 더 이상 연산이 의미가 없을 때
        if n == 0:
            # for i in range(12)
            break
    # 2진수로의 변환이 완료되지 않으면
    if n != 0:
        print(f"#{tc} overflow")
    # 2진수 변환이 정상적으로 완료됐을 때
    else:
        print(f"#{tc} {binary_str}")
