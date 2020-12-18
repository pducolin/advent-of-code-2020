DEBUG = False


def dbg_print(s):
    if DEBUG:
        print(s)


def parse_number(expression):
    number_str = ''
    dbg_print(f'Parsing number in {expression}')
    while len(expression) > 0 and expression[0].isdigit():
        number_str += expression[0]
        expression = expression[1:] if len(expression) > 1 else ''

    dbg_print(f'Parsed number {number_str}, expression: {expression}')
    return int(number_str), expression


def parse_group(expression):
    if expression[0] != '(':
        raise Exception('Invalid group start: {}'.format(expression[0]))
    dbg_print(f'Parsing group in {expression}')
    expression = expression[1:] if len(expression) > 1 else ''
    group = ''
    while len(expression) > 0:
        ch = expression[0]
        if ch.isdigit() or ch == '+' or ch == '*':
            group += ch
            expression = expression[1:] if len(expression) > 1 else ''
            continue
        if ch == '(':
            subgroup, expression = parse_group(expression)
            value = evaluate_expression(subgroup)
            group += str(value)
            continue
        if ch == ')':
            expression = expression[1:] if len(expression) > 1 else ''
            dbg_print(f'Parsed group {group}, expression: {expression}')
            return group, expression
    raise Exception('No closure for group')


def evaluate_expression(expression):
    result = None
    current_operation = None
    # remove all spaces
    expression = expression.replace(' ', '')
    dbg_print(f"Evaluate expression {expression}")
    while len(expression) > 0:
        ch = expression[0]
        if ch == '+':
            current_operation = ch
            expression = expression[1:] if len(expression) > 1 else ''
            continue
        if ch == '*':
            # first solve all sums
            if '+' in expression:
                value = evaluate_expression(expression[1:])
                expression = str(result) + '*' + str(value)
                continue
            current_operation = ch
            expression = expression[1:] if len(expression) > 1 else ''
            continue
        value = None
        if ch == '(':
            group, expression = parse_group(expression)
            value = evaluate_expression(group)
        elif ch.isdigit():
            value, expression = parse_number(expression)

        if current_operation == '+':
            result += value
            current_operation = None
        elif current_operation == '*':
            result = result * value
            current_operation = None
        else:
            result = value
        continue

    dbg_print(f'Expression result: {result}')
    return result


def solve_expression_list(expression_list):
    return sum([evaluate_expression(x) for x in expression_list])


def solution(data):
    return solve_expression_list(data.splitlines())
