""" This module provides a function to calculate a mathematical
expression given as a Ukrainian sentence.
"""

def calculate_expression(expression: str) -> int | str | None:
    """
    Calculate the mathematical expression and return the result of it.

    param expression: str, mathematical expression
    return: int, the result of calculation, or str if input is invalid,
            or None if input isn't a string.
    >>> calculate_expression('Скільки буде 8 відняти 3?')
    5
    >>> calculate_expression('Скільки буде 7 додати 3 помножити на 5?')
    50
    >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -3?')
    9
    >>> calculate_expression('Скільки буде 3 в кубі?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде...')
    'Неправильний вираз!'
    >>> calculate_expression('3 поділити на 3?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки сезонів у році?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 10 додати додати 9?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 2 2 додати?')
    'Неправильний вираз!'
    >>> calculate_expression('')
    'Неправильний вираз!'
    >>> calculate_expression(123 + 33)
    """
    if not isinstance(expression, str):
        return None

    spased_exp = expression.replace('?', ' ?')
    words = spased_exp.split()
    exp_words = words[2:-1]


    try:
        if len(words) < 6 and words[0] != 'Скільки' or words[1] != 'буде' or words[-1] != '?':
            return 'Неправильний вираз!'
        # if exp_words[1] == 'в' and exp_words[2] == 'кубі' or exp_words[2] == 'квадраті':
        #     return 'Неправильний вираз!'

        # if exp_words[0].isdigit is False: # дописати для друго числа
        #     return 'Неправильний вираз!'

        total = int(exp_words[0])
        i = 1
        while i < len(exp_words):

            if exp_words[i] == 'додати' or exp_words[i] == 'плюс':
                total += int(exp_words[i+1])
                i += 2
            elif exp_words[i] == 'відняти' or exp_words[i] == 'мінус':
                total -= int(exp_words[i+1])
                i += 2
            elif exp_words[i] == 'помножити':
                if exp_words[i+1] == 'на':
                    total *= int(exp_words[i+2])
                    i += 3
                else:
                    return 'Неправильний вираз!'
            elif exp_words[i] == 'поділити':
                if exp_words[i+1] == 'на':
                    num = int(exp_words[i+2])
                    if num == 0:
                        raise ValueError('Неправильний вираз!')
                    total //= num
                    i += 3
                else:
                    return 'Неправильний вираз!'
            else:
                raise ValueError('Неправильний вираз!')
        return total
    except (ValueError, IndexError, IndexError):
        return 'Неправильний вираз!'


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
