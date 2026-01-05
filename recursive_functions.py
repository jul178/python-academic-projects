# def create_table(n: int, m: int) -> list[list]:
#     """Function create the table of numbers with size n * m.

#     Args:
#         n (int): Number of rows of the table.
#         m (int): Number of columns of the table.
#     Returns:
#         list[list]: List of lists.
#     >>> create_table(4,6)
#     [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], \
# [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
#     """
#     # for i in range(n):
#     #     for j in range(m):
#     #         if i == 0 or j == 0:
#     #         # if n[0] == 1 or m[0] == 1:
#     #             i[0] = 1
#     #             j[0] = 1
#     if n == 1:
#         return [[1] * m]
#     table = create_table(n - 1, m)
#     row = table[-1]
#     new_row = [1] * m
#     for j in range(m):
#         if j == 0:
#             new_row[j] = 1
#         else:
#             new_row[j] = row[j] + new_row[j-1]
#     table.append(new_row)
#     return table

# def flatten(lst: list[list]) -> list:
#     """Recursively flattens a nested list into a single list of values.

#     Args:
#         lst (list[list] | Any): List of lists.
#     Returns:
#         list | Any: List consist of all non-empty elements of each of the input lists.
#             The elemants ordered in the same way as in original list.
#             If a non-list was passed, the arguments itself returned.

#     >>> flatten([1, [2]])
#     [1, 2]
#     >>> flatten([1, 2, [3, [4, 5], 6], 7])
#     [1, 2, 3, 4, 5, 6, 7]
#     >>> flatten(['wow', [2, [[]]], [True]])
#     ['wow', 2, True]
#     >>> flatten([])
#     []
#     >>> flatten([[]])
#     []
#     >>> flatten(3)
#     3
#     """
#     flatten_list = []
#     if not isinstance(lst, list):
#         return lst
#     for element in lst:
#         if not isinstance(element, list):
#             flatten_list.append(element)
#         if isinstance(element, list):
#             flatten_list.extend(flatten(element))
#     return flatten_list


# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())





# def sum_nested(nested_list):
#     if not nested_list:
#         return 0
#     list_of_elem = []
#     for el in nested_list:
#         if not isinstance(el, list):
#             list_of_elem.append(el)
#         if isinstance(el, list):
#             list_of_elem.append(sum_nested(el))
#     return sum(list_of_elem)



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))
