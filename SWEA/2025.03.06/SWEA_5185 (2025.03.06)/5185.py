# SWEA 5185 이진수 (2025.03.06)
# import sys

hex_dict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}
# sys.stdin = open("5185_input.txt", "r")
# sys.stdout = open("5185_my_output.txt", "w")
T = int(input())
for tc in range(1, T + 1):
    N, hex_str = input().split()
    n = int(N)
    print(f"#{tc}", end=" ")
    for i in range(n):
        # 16진수를 10진수로 변환
        hex_dec = hex_dict[hex_str[i]]
        # 변환된 이진수를 저장할 문자열
        binary_str = ""
        # 4자리의 이진수 변환
        for _ in range(4):
            # 앞쪽에 추가하여 순서 유지
            binary_str = str(hex_dec % 2) + binary_str
            hex_dec //= 2
        print(binary_str, end="")
    print()
