# SWEA 괄호 짝짓기 (2025.03.02)
# 괄호 짝 비교를 위한 dict
compare_dict = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
for tc in range(1, 11):
    N = int(input())
    my_str = input()
    stack = [None] * N
    top = -1
    for s in my_str:
        # 여는 괄호일 때
        if s in "([{<":
            top += 1
            stack[top] = s
        # 닫는 괄호일 때
        elif s in ")]}>":
            # stack이 비었거나 괄호 짝이 안 맞을 때
            if top == -1 or stack[top] != compare_dict[s]:
                print(f"#{tc} {0}")
                break # for s in my_str
            top -= 1
            stack[top + 1] = None
    else:
        # stack이 비어있지 않을 때 고려
        print(f"#{tc} {1 if top == -1 else 0}")
