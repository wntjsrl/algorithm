# SWEA 비밀번호 (2025.03.02)
for tc in range(1, 11):
    N, my_str = input().split()
    stack = [None] * int(N)
    top = -1
    for s in my_str:
        # stack이 비었거나 다른 문자일 때
        if top == -1 or s != stack[top]:
            top += 1
            stack[top] = s
        # 같은 문자일 때
        elif s == stack[top]:
            top -= 1
            stack[top + 1] = None
    print(f"#{tc} {''.join(stack[:top + 1])}")
