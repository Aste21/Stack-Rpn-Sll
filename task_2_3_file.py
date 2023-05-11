# minusy i floaty dodaj pls dzienki
# nmza co mordo pzdr

from stack_file import Stack

operators = ('+', '-', '*', '/', '(', ')', ',')
operators_value = {'+': 2, '-': 2, '/': 1, '*': 1}


def is_number(ch):
    is_digit_inside = False
    is_dot_inside = False
    if ch[-1] == '.':
        return False
    for i in range(len(ch)):
        if ch[i].isdigit():
            is_digit_inside = True
        if ch[i] == '-' and i != 0:
            return False
        if ch[i] == '.' and not is_digit_inside:
            return False
        if ch[i] == '.' and is_dot_inside:
            return False
        if ch[i] != '-' and not ch[i].isdigit() and ch[i] != '.':
            return False
        if ch[i] == '.':
            is_dot_inside = True
    if not is_digit_inside:
        return False
    return True


def get_input(string_f, user_input):
    global operators
    is_last_space = True
    j = 0
    num_of_open = 0
    num_of_closed = 0
    for i in range(len(user_input)):
        if ord(user_input[i]) != 32:
            if user_input[i] == '(':
                num_of_open += 1
            if user_input[i] == ')':
                num_of_closed += 1
            if user_input[i] in operators or is_number(user_input[i]) or user_input[i] == '.':
                if is_last_space:
                    string_f.push(user_input[i])
                    is_last_space = False
                else:
                    string_f.stack[j] += user_input[i]
        else:
            is_last_space = True
            j += 1
    if num_of_closed != num_of_open:
        print("ERROR: PROBLEM WITH '(' AND ')'")
        return 'error'


def convert_to_postfix(stack):
    global operators, operators_value
    operators_temp = Stack(100, str)
    result = Stack(100, str)
    operators_temp.push('(')
    j = 0

    while j < len(stack.stack):
        popped = stack.stack[j]

        if is_number(popped):
            result.push(popped)
        elif popped == '(':
            operators_temp.push('(')
        elif popped == ')':
            temp = operators_temp.pop()
            while temp != '(':
                result.push(temp)
                temp = operators_temp.pop()
        elif popped in operators:
            if operators_temp.top() != '(' and operators_temp.top != ')':
                if operators_value[popped] <= operators_value[operators_temp.top()]:
                    result.push(operators_temp.pop())
                    operators_temp.push(popped)
                else:
                    operators_temp.push(popped)
            else:
                operators_temp.push(popped)
        j += 1

    popped = operators_temp.pop()
    while len(operators_temp.stack) != 0 and popped != '(':
        result.push(popped)
        popped = operators_temp.pop()

    return result


def calculate_postfix(stack, type_of_data):
    temp_stack = Stack(100, type_of_data)
    for i in range(len(stack.stack)):
        if is_number(stack.stack[i]):
            temp_stack.push(type_of_data(stack.stack[i]))
        else:
            if temp_stack.is_empty():
                print("ERROR: WRONG AMOUNT OF CHARACTERS 1")
                return 'error'
            a = temp_stack.pop()
            if temp_stack.is_empty():
                print("ERROR: WRONG AMOUNT OF CHARACTERS 2")
                return 'error'
            b = temp_stack.pop()
            match stack.stack[i]:
                case '+':
                    temp_stack.push(a + b)
                case '-':
                    temp_stack.push(b - a)
                case '*':
                    temp_stack.push(a * b)
                case '/':
                    temp_stack.push(b / a)
    if temp_stack.top_in == 0:
        return temp_stack.top()
    else:
        print("ERROR: WRONG AMOUNT OF CHARACTERS 3")
        return 'error'
