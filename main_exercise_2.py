from exercise_2_file import *
from stack_file import Stack
from singly_linked_list_file import *

potential_palindrome = input()

first_half = SLL()
second_half = Stack(100, str)

get_sll_input(first_half, potential_palindrome[0:len(potential_palindrome) // 2])
get_stack_input(second_half, potential_palindrome[len(potential_palindrome) -
                                                  len(potential_palindrome) // 2:len(potential_palindrome)])

print(check_if_palindrome(first_half, second_half))
