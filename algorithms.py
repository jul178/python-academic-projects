# ////// selection sort
# def swap(l, i, j):
#     temp =l[j]
#     l[i] = l[j]
#     # l[j] = temp
#     l[i], l[j] = l[j], l[i]

# print(a)
# swap(a, 0, 1)
# swap(a, 0, 2)
# print(a)

"""Algoritm of search and sort"""
import random
def linear_search(list_of_values, value):
    """
    Performs a linear search to find the index of a value in a list.

    Args:
        list_of_values: The list to search through.
        value: The value to search for.

    Returns:
        int: The index of the value if found, otherwise -1.

    Examples:
        >>> linear_search([2, 3, 4, 5], 4)
        2
        >>> linear_search([10, 20, 30], 5)
        -1
        >>> linear_search([], 1)
        -1
    """
    for cur_i, cur_v in enumerate(list_of_values):
        if cur_v == value:
            return cur_i
    return -1
result = linear_search([2, 3, 4, 5], 4)
print("Linear search:")
print(result)


def selection_sort(lst):
    """
    Sorts a list using the Selection Sort algorithm.

    Args:
        lst: A list of integers (unsorted).

    Returns:
        List[int]: A new sorted list (or modified list depending on implementation).

    Examples:
        >>> selection_sort([9, 1, 8, 2, 7])
        [1, 2, 7, 8, 9]
        >>> selection_sort([3, 3, 1])
        [1, 3, 3]
        >>> selection_sort([])
        []
    """
    for i, el in enumerate(lst):
        min_i = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_i]:
                min_i = j

        # lst[i], lst[min_i] = lst[min_i], lst[i]
        lst[i], lst[min_i] = lst[min_i], el
    return lst

unsorted = [9, 1, 8, 2, 7, 3, 6, 4, 5]
print("Unsorted:")
print(unsorted)
sorted_lsr = selection_sort(unsorted)
print("Selection sort:")
print(sorted_lsr)


# def linear_search(list_of_values, value):
#     """Linear search"""
#     for i in range(len(list_of_values)):
#         if value == list_of_values[i]:
#             return i
#     return -1
# result = linear_search([2, 3, 4, 5], 4)
# print("Linear search:")
# print(result)

def binary_search(list_of_values, value):
    """
    Performs a binary search on a SORTED list.

    Args:
        list_of_values: A sorted list of integers.
        value: The value to search for.

    Returns:
        int: The index of the value if found, otherwise -1.

    Examples:
        >>> binary_search([2, 3, 4, 5], 3)
        1
        >>> binary_search([1, 5, 8, 10, 15], 15)
        4
        >>> binary_search([1, 2, 3], 9)
        -1
        >>> binary_search([], 1)
        -1
    """
    m = len(list_of_values)//2
    l = 0
    r = len(list_of_values) - 1
    while l <= r:
        m = (l + r)//2

        if list_of_values[m] == value:
            return m
        # elif l == r:
        #     return -1
        if list_of_values[m] < value:
            #move left limit
            l = m + 1
        elif list_of_values[m] > value:
            #move right limit
            r = m - 1
    return -1

result = binary_search([2, 3, 4, 5], 3)
print("Binary search:")
print (result)

def quick_sort(lst):
    """
    Sorts a list using the Quick Sort algorithm.

    Args:
        lst: A list of integers.

    Returns:
        List[int]: A new sorted list.

    Examples:
        >>> quick_sort([9, 1, 8, 2, 7, 3, 6, 4, 5])
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> quick_sort([10, 5, 2, 3])
        [2, 3, 5, 10]
        >>> quick_sort([])
        []
    """
    if len(lst) == 0 or len(lst) == 1:
        return lst
    pivot = random.sample(lst, 1)[0]
    left, right = [], []
    counter = 0
    for elem in lst:
        if elem < pivot:
            left.append(elem)
        elif elem > pivot:
            right.append(elem)
        else:
            counter += 1
    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] * counter + right

quick_srt = quick_sort(unsorted)
print("Quick sort:")
print(quick_srt)

# def quick_sort2(lst):
#     return quick_sort2([el for el in lst if el < el[0]]) + lst.count

def merge_sort(lst):
    """
    Sorts a list using the Merge Sort algorithm.

    Args:
        lst: A list of integers.

    Returns:
        List[int]: A new sorted list.

    Examples:
        >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
        [3, 9, 10, 27, 38, 43, 82]
        >>> merge_sort([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left_half = lst[:mid]
    right_half = lst[mid:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def merge(left, right):
    """
    Helper function for merge_sort. Merges two sorted lists.

    Examples:
        >>> merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    sorted_list = []
    l = 0 # індекс для left
    r = 0 # індекс для right
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1
    sorted_list.extend(left[l:])
    sorted_list.extend(right[r:])
    return sorted_list

unsorted = [38, 27, 43, 3, 9, 82, 10]
merge_srt = merge_sort(unsorted)
print("Merge sort:")
print(merge_srt)


def insertion_sort(lst):
    """
    Sorts a list using the Insertion Sort algorithm.

    Args:
        lst: A list of integers.

    Returns:
        List[int]: The sorted list.

    Examples:
        >>> insertion_sort([5, 2, 4, 6, 1, 3])
        [1, 2, 3, 4, 5, 6]
        >>> insertion_sort([10, 1])
        [1, 10]
        >>> insertion_sort([1, 2, 3])
        [1, 2, 3]
    """
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst

insert_srt = insertion_sort(unsorted)
print("Insertion sort:")
print(insert_srt)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
