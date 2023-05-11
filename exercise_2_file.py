def get_sll_input(sll, user_input):
    for i in range(len(user_input)):
        sll.add_node(user_input[i])


def get_stack_input(stack, user_input):
    for i in range(len(user_input)):
        stack.push(user_input[i])


def check_if_palindrome(f_half, s_half):
    while f_half.size > 0 and len(s_half.stack) > 0:
        if f_half.first_out() != s_half.pop():
            return False
    return True
