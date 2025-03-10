# SWEA 4408 자기 방으로 돌아가기 (2025.03.10)

# import sys

# sys.stdin = open("4408_input.txt", "r")
# sys.stdout = open("4408_my_output.txt", "w")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N)]
    hallway = [0] * 201
    for s in students:
        start, end = sorted([(s[0] + 1) // 2, (s[1] + 1) // 2])
        for i in range(start, end + 1):
            hallway[i] += 1
    print(f"#{tc} {max(hallway)}")
