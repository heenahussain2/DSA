"""
Challenge 100 Doors:
Imagine you have 100 doors in a row, all initially closed.
You make 100 passes by these doors.
On the first pass, you toggle the state of every door
(if it's closed, you open it; if it's open, you close it).
On the second pass, you toggle every second door (2, 4, 6, 8...)
On the third pass, you toggle every third door (3, 6, 9...) and so on,
until the 100th pass where you only toggle the 100th door.

The challenge is to determine which doors are open at the end of this process.
"""
# All doors are closed at the start
# Taking 101 so we start from 1 position and don't have to use offset
doors = [False] * 101

# The first loop is for the pass
for pass_no in range(1, 101):
    # The second loop is to toggle the state of the door
    for i in range(pass_no, 101, pass_no):
        doors[i] = not doors[i]


# print the doors that are open
for j in range(1, 101):
    if doors[j]:
        print(j, end=", ")
