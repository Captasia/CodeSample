# return the priority of bodmas
def bodmas(operator):
    match operator:
        case "+" | "-":
            return 1
        case "*" | "/":
            return 2
        case "^":
            return 3
    return 0

# helper function for basic equation on token
def equate(operator, a, b):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case "^":
            return a ** b

# converting infix equation to postfix equation
def convert2PostFix(infix):
    stack = []
    output = []
    lastDigits = ""
    for char in infix:
        if char == ' ':
            continue
        if char.isdigit() or char == ".":
            lastDigits += char
        else:
            if (lastDigits):
                output.append(lastDigits)
                lastDigits = ""
            if char.isalpha():
                output.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while (stack and bodmas(stack[-1]) >= bodmas(char)):
                    output.append(stack.pop())
                stack.append(char)
    
    if lastDigits:
        output.append(lastDigits)

    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)

# calculate infix equation
def calculate(infix):
    stack = []
    postfix = convert2PostFix(infix)
    tokens = postfix.split()
    for token in tokens:
        try:
            stack.append(float(token))
        except ValueError:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = equate(token,operand1, operand2)
            stack.append(result)
    return stack.pop()




infix = "(32 + 5) * 2.5 ^ 3 - 8 / 4"
print(calculate(infix))