"""Construct a list of lucky numbers that do not exceed a given number n"""
def sieve_flavius(n: int) -> list[int]:
    '''Generates a list of lucky numbers not exceeding the given number n.

    Parameters:
    n (int): The upper limit for generating lucky numbers.

    Returns:
    list[int]: A list of lucky numbers up to n.

    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(33)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    '''
    if n == 0:
        return []
    if isinstance(n, int) and n > 0:
        list_lucky_num = []

        for i in range(1, n + 1, 2):
            list_lucky_num.append(i)
        # print(list_lucky_num)
        step_index = 1
        while step_index < len(list_lucky_num):
            removal_step = list_lucky_num[step_index]

            if removal_step >= len(list_lucky_num):
                break

            for index in range(len(list_lucky_num)-1, -1, -1):
                if (index + 1) % removal_step == 0:
                    list_lucky_num.pop(index)

            # print(list_lucky_num)
            step_index += 1
        return list_lucky_num
    return None


# print(sieve_flavius(100))


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
