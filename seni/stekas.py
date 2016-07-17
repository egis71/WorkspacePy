# Function to check closes of parentheses
def closes(left, right):
    return left == '(' and right == ')' or \
        left == '{' and right == '}' or \
        left == '[' and right == ']'


def check(inputs):
    inputs = inputs.strip()
    if len(inputs) == 0:
        return True
    if len(inputs) % 2 != 0:
        return False
    stack = []
    for c in inputs:
        if len(stack) == 0:
            stack.append(c)
            continue
        if closes(stack[-1], c):
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0


test1 = '(({})[])'
test2 = '([)]'

for t in [test1, test2]:
    print("Testo '%s' rezultatas %s" %
          (t, check(t)))

input()
