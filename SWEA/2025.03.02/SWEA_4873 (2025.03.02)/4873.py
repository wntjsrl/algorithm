# SWEA 4873 반복문자 지우기 (2025.03.02)
T = int(input())
for tc in range(1, T + 1):
    my_str = input()
    N = len(my_str)
    stack = [None] * N
    top = -1
    for i in range(N):
        # 스택이 비었거나, 다음 문자와 다르면 push
        if top == -1 or my_str[i] != stack[top]:
            top += 1
            stack[top] = my_str[i]
        # 다음 문자와 같으면 pop
        elif my_str[i] == stack[top]:
            top -= 1
            stack[top + 1] = None
    print(f"#{tc} {top + 1}")
