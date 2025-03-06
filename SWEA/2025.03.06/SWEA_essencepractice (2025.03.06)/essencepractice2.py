# SWEA essencepractice2 (2025.03.06)
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
# sys.stdin = open("essencepractice2_input.txt", "r")
# sys.stdout = open("essencepractice2_my_output.txt", "w")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    hex_str = input()
    # 16진수를 2진수로 변환
    binary_str = "".join(f"{hex_dict[c]:04b}" for c in hex_str)
    # 2진수를 10진수로 변환
    M = len(binary_str)
    decimal_numbers = []
    for i in range(0, M - M%7, 7):
        decimal_numbers.append(int(binary_str[i:i + 7], 2))
    print(f"#{tc}", *decimal_numbers)
