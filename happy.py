"""Search for lucky tram tickets"""
def happy_number(number: int) -> bool:
    """
    Determines if a ticket number is a happy number.

    Parameters:
    num (int): The ticket number to check.

    Returns:
    bool: True if the ticket is a happy number, False otherwise.

    >>> happy_number(1234)
    False
    >>> happy_number(32100123)
    True
    >>> happy_number(159123)
    True
    """
    if isinstance(number, int) and number >= 0:
        number_str = str(number)
        if len(number_str) < 8:
            zeros = 8 - len(number_str)
            number_str = ('0' * zeros) + number_str
            # print(number_str)
        elif len(number_str) > 8:
            return None

        sum_half_1 = 0
        sum_half_2 = 0

        for i in number_str[:4]:
            sum_half_1 += int(i)
        # print(sum_half_1)


        for j in number_str[4:]:
            sum_half_2 += int(j)
        # print(sum_half_2)

        while sum_half_1 > 9 or sum_half_2 > 9:
            sum_half_1_dig = 0
            sum_half_2_dig = 0
            for i in str(sum_half_1):
                sum_half_1_dig += int(i)
            sum_half_1 = sum_half_1_dig

            for j in str(sum_half_2):
                sum_half_2_dig += int(j)
            sum_half_2 = sum_half_2_dig

        # print(sum_half_1, sum_half_2)

        return sum_half_1 == sum_half_2

    return None




def count_happy_numbers(n: int) -> int:
    """
    Counts the number of happy tickets from 1 to n inclusive.

    Parameters:
    n (int): The upper limit of ticket numbers to check.

    Returns:
    int: The count of happy tickets in the range.

    >>> count_happy_numbers(10001)
    1
    >>> count_happy_numbers(10010)
    2
    >>> count_happy_numbers(10100)
    12
    >>> count_happy_numbers(100000)
    9999
    """
    if isinstance(n, int) and n >= 0:
        counter = 0
        for i in range(1, n + 1):
            is_happy = happy_number(i)
            if is_happy:
                counter += 1
        return counter
    return None




def happy_numbers(m: int, n: int) -> list[int]:
    """
    Generates a list of happy ticket numbers within the given range.

    Parameters:
    m (int): The lower limit of ticket numbers (inclusive).
    n (int): The upper limit of ticket numbers (inclusive).

    Returns:
    list[int]: A list of happy ticket numbers in the range.

    >>> happy_numbers(1, 10001)
    [10001]
    >>> happy_numbers(10001, 10010)
    [10001, 10010]
    >>> happy_numbers(1, 11)
    []
    >>> happy_numbers(10001, 10100)
    [10001, 10010, 10019, 10028, 10037, 10046, 10055, 10064, 10073, 10082, 10091, 10100]
    """
    list_happy_tickets = []
    for k in range(m, n + 1):
        if happy_number(k):
            list_happy_tickets.append(k)
    return list_happy_tickets




if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
