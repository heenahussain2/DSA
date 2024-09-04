"""
Quicksort Algorithm
- Quicksort is an efficient and powerful algorithm for sorting data.
- It is a recursive algorithm and is based on divide and conquer.
- Some variant of this algorithm is used in libraries for several
common programming languages.

"""


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


data = [3, 1, 4, 2]
print(quicksort(data))

# What about data with duplicates?
data = [1, 6, 5, 5, 2, 6, 1]
print(quicksort(data))
