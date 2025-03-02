# SWEA 4866 괄호검사 (2025.03.02)
T = int(input())
for tc in range(1, T + 1):
    my_str = input()
    N = len(my_str)
    # 괄호의 짝이 맞는지 확인하기 위한 dict
    compare_dict = {
        ")": "(",
        "}": "{"
    }
    stack = [None] * N
    top = -1
    for i in range(N):
        # 여는 괄호일 때 push
        if my_str[i] in "({":
            top += 1
            stack[top] = my_str[i]
        # 닫는 괄호일 때
        elif my_str[i] in ")}":
            # stack이 비어 있거나, 괄호의 짝이 맞지 않을 때
            if top == -1 or stack[top] != compare_dict[my_str[i]]:
                print(f"#{tc} {0}")
                break # for i in range(N)
            top -= 1
            stack[top + 1] = None
    else:
        # 스택이 비어야 유효
        print(f"#{tc} {1 if top == -1 else 0}")
