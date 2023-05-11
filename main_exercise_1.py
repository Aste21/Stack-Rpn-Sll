from task_2_3_file import *

s = Stack(30, str)
input = input()
print(str(input))
is_error = get_input(s, str(input))

if not is_error:
    print(s.stack)

    s = convert_to_postfix(s)

    print(s.stack)

    value = calculate_postfix(s, float)
    if value != 'error':
        print(f"The result is: {value}")
