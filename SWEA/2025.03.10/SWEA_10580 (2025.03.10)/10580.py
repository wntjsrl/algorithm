# SWEA 10580 전봇대 (2025.03.10)

# import sys

# sys.stdin = open("10580_input.txt", "r")
# sys.stdout = open("10580_my_output.txt", "w")

T = int(input())
for tc in range(1, T + 1):
    # 선의 갯수
    N = int(input())
    """
    1. N개의 새로운 선을 추가하면서 비교 진행
        기존 선들과 저장하면서 진행
    2. 비교 = 기존 선들과 비교
    """
    # 선 추가
    # 기존 선들을 저장할 리스트
    wires = []
    # 교차점의 갯수
    answer_count = 0
    for _ in range(N):
        start, end = map(int, input().split())
        # 기존 연결된 선들과 비교
        for prev_start, prev_end in wires:
            # 교차점 조건 1
            """
            기존의 전선보다 시작점이 높고, 도착점이 낮음
            """
            if start > prev_start and end < prev_end:
                answer_count += 1
            # 교차점 조건 2
            """
            기존의 전선보다 시작점이 낮고, 도착점이 높음
            """
            if start < prev_start and end > prev_end:
                answer_count += 1
        # 목록에 전선을 추가
        wires.append([start, end])
    print(f"#{tc} {answer_count}")
