n = int(input())
stack = []

for i in range(0, n):
    s = str(input())
    li = list(s)

    for j in range(len(li)):
        if li[j] == '(':
            stack.append('(')

        if not stack and li[j] == ')':
            stack.append(')')
            break

        if stack and li[j] == ')':
            stack.pop(-1)

    if not stack:
        print("YES")
        stack.clear()

    elif stack:
        print("NO")
        stack.clear()
