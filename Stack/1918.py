expr = input().strip()

post = []
stack = []
for i in range(len(expr)):
    if expr[i] >= 'A' and expr[i] <= 'Z':
        post.append(expr[i])
    else:
        if expr[i] == "(":
            stack.append('(')
        elif expr[i] in ['*', '/']:
            while stack and stack[-1] in ['*', '/']:
                post.append(stack.pop())
            stack.append(expr[i])
        elif expr[i] in ['+', '-']:
            while stack and stack[-1] in ['+', '-']:
                post.append(stack.pop())
            stack.append(expr[i])
        elif expr[i] == ')':
            while stack and stack[-1] != '(':
                post.append(stack.pop())
            stack.pop()

while stack:
    post.append(stack.pop())
            
print("".join(post))