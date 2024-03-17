def get_sum(input_expression):
    elements = input_expression.split()
    stack = []

    for element in elements:
        if element.isdigit():
            stack.append(int(element))
        else:
            right = stack.pop()
            left = stack.pop()

            match element:
                case '+':
                    stack.append(left + right)
                case '-':
                    stack.append(left - right)
                case '*':
                    stack.append(left * right)
                case '/':
                    stack.append(left // right)
                case '%':
                    stack.append(left % right)

    result_sum = stack[0]

    return result_sum


input_expression = input()

print(get_sum(input_expression))
