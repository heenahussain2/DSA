
"""
Objective:
- The goal is to place numbers in a sequence so that all
- inequality signs (like < and >) between them are correct.

Transform and Conquer:
- First, sort the numbers in descending order (from largest to smallest).

Using Two Pointers:
- Imagine you have two markers (pointers) at the start and end of
the sorted list.
- These markers help you pick the smallest or largest number based
on the inequality sign.
    - If you see a < sign, pick the smallest remaining number.
    - If you see a > sign, pick the largest remaining number.
- Move the marker after using a number to "delete" it from the list.
"""
import random


PUZZLE_SIZE = 10

# Create a list with random numbers
# random.sample ensures no duplicates
puzzle_nums = random.sample(range(100), PUZZLE_SIZE)
puzzle_symbols = []
solution = []

for i in range(PUZZLE_SIZE - 1):
    puzzle_symbols.append(">" if random.random() < 0.5 else "<")

# sort the numbers in descending order
sorted_puzzle_nums = sorted(puzzle_nums, reverse=True)

# define low and high pointers
low = PUZZLE_SIZE - 1  # will be at the end
high = 0  # will be at the start since array is sorted in reverse

for symbol in puzzle_symbols:
    if symbol == "<":
        solution.append(str(sorted_puzzle_nums[low]))
        solution.append(symbol)
        low -= 1
    elif symbol == ">":
        solution.append(str(sorted_puzzle_nums[high]))
        solution.append(symbol)
        high += 1

# Add the remaining number at the end of the solution array
solution.append(str(sorted_puzzle_nums[low]))


# Display Solution
print(" ".join(solution))
# Evaluate the solution
print(eval(" ".join(solution)))
