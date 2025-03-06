# SWEA binarypassword (2025.03.06)
# import sys

def solve(N, M, password):
    # 암호 구간 찾기 위한 순회
    # 가장 윗 행부터 검사
    for i in range(N):
        # 가장 뒷 열부터 검사
        for j in range(M - 1, -1, -1):
            # 암호 구간 찾으면
            if password[i][j] == "1":
                # 암호 저장할 리스트
                password_arr = []
                # 짝수 인덱스 암호 합
                even_sum = 0
                # 홀수 인덱스 암호 합
                odd_sum = 0
                # 뒷 열부터 암호 읽기
                for k in range(j, j - 56, -7):
                    password_arr.append(bin_dict[password[i][k - 6:k + 1]])
                for i in range(len(password_arr)):
                    # 짝수 인덱스의 암호일 떄
                    if i % 2 == 0:
                        even_sum += password_arr[i]
                    # 홀수 인덱스의 암호일 때
                    else:
                        odd_sum += password_arr[i]
                # 암호 조건을 만족하면 전체 암호 합 반환
                # 그렇지 않으면 0 반환
                return sum(password_arr) if (odd_sum*3 + even_sum) % 10 == 0 else 0

# 암호 해독을 위한 딕셔너리
bin_dict = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

# sys.stdin = open("binarypassword_input.txt", "r")
# sys.stdout = open("binarypassword_my_output.txt", "w")
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    password = [input() for _ in range(N)]
    print(f"#{tc} {solve(N, M, password)}")
