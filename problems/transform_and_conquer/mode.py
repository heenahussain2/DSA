"""
The mode is the most common number that appears in your set of data.
To find the mode count how often each number appears and the number that
appears the most times is the mode.

In this method we will sort the array first and then count the occurrences
of that number by looping through the array until it finds a different number.
"""


def mode_presort(arr: list):
    arr.sort()
    mode_frequency = 0  # current highest frequency
    i = 0  # array index
    while i < len(arr):
        current_number = arr[i]
        # This will count the number of time each element occurs
        num_counter = 1
        # Loop Until you encounter a different number
        while (i + num_counter < len(arr) and
               arr[i + num_counter] == current_number):
            num_counter += 1
            # If the mode of current number exceeds the previous mode
            # then update it with the current mode value
            if num_counter > mode_frequency:
                mode_frequency = num_counter
                mode_value = [current_number]
            # If two elements have same mode or the same number
            # of occurrences
            elif num_counter == mode_frequency:
                mode_value.append(current_number)
        i += num_counter
    return mode_value


arr = [1, 1, 1, 2, 2]
print(mode_presort(arr))
arr = [1, 1, 2, 2]
print(mode_presort(arr))
arr = [3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]
print(mode_presort(arr))
