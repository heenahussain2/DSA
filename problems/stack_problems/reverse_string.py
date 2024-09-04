"""
In this problem we will use a stack to reverse a string
This is called as accumulator pattern in which:
    - we start with an "empty bucket" of the right data type,
    - and build the solution by filling the bucket within a loop
"""
from data_structures import stack


def reverse_string(my_string):
    reversed_string = ""
    # initialize the stack DS
    s = stack.Stack()
    # add the characters to the stack one by one
    for char in my_string:
        s.push(char)

    # Now empty the stack and add the chars to string
    while not s.is_empty():
        reversed_string += s.pop()

    return reversed_string


while True:
    input_str = input("Enter the string: ")
    if input_str == "exit":
        break
    print("Reversed string: ", reverse_string(input_str))
