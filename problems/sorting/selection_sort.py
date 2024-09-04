"""
Selection Sort
- Find the smallest element in the array and exchange it with the first element
- Find the second smallest element and exchange it with the element in the
2nd position
- Repeat it until the array is sorted

Find Minimum Value
- Create a variable called min_index and set it to 0
- Iterate through the list, and if a value is less than the one at min_index,
update min index to the new position.
"""


def selection_sort(xs):
    for i in range(len(xs)):
        min_index = i
        # find the smallest value
        for j in range(i+1, len(xs)):
            if xs[j] < xs[min_index]:
                min_index = j
        xs[i], xs[min_index] = xs[min_index], xs[i]

    return xs


xs = [3, 2, 1, 5, 4]
print(selection_sort(xs))
