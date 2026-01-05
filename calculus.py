"""Different calculus functions"""
def find_max_value(func: callable, points: list[float]) -> float:
    """Find the maximal value of a function at given points.

    Args:
        func (callable): The function to evaluate.
        points (list[float]): A list of points at which to evaluate the function.

    Returns:
        float: The maximal value of the function at the given points
               round to 2 decimal points.

    Examples:

    >>> find_max_value(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    return round(max(map(func, points)), 2)


def find_max_points(func: callable, points: list[float]) -> set[float]:
    """Find the points where the function has the maximal value.

    Args:
        func (callable): The function to evaluate.
        points (list[float]): A list of points at which to evaluate the function.

    Returns:
        set[float]: A set of points where the function has the maximal value.

    Examples:
    >>> find_max_points(lambda x: x ** 2 + x, [1, 2, 3, -1])
    {3}
    >>> find_max_points(lambda x: -x ** 2 + 4*x, [1, 0, 3, -1])
    {1, 3}
    """
    max_points = set()
    for point in points:
        if max(list(map(func, points))) == func(point):
            max_points.add(point)
    return max_points

def compute_limit(seq: callable) -> float:
    """Compute the limit of a convergent sequence.

    Args:
        seq (callable): A function representing the sequence.

    Returns:
        float: The limit of the sequence rounded up to 2 decimal points.

    Examples:
        >>> compute_limit(lambda n: (n ** 2 + n) / (3*n ** 2))
        0.33
    """
    n = 10**5
    result = seq(n)
    for _ in range(5):
        next_result = seq(n)
        if next_result - result <= 10**(-3):
            return round(seq(n), 2)



def compute_derivative(func: callable, x_0: float) -> float:
    """Compute the derivative of a function at a given point.

    Args:
        func (callable): The function to differentiate.
        x_0 (float): The point at which to compute the derivative.

    Returns:
        float: The derivative of the function at the given point.

    Examples:
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    return round((func(x_0 + 10**(-5)) - func(x_0)) / (10**(-5)), 2)


def get_tangent(func: callable, x_0: float) -> str:
    """Calculate the equation of the tangent line to a given function at a specified point.

    This function computes the tangent line to the input function `func` at the point `x_0`.
    The tangent line is represented in the form of a linear equation.

    Args:
        func (callable): A function for which the tangent line is to be calculated.
        x_0 (float): The x-coordinate at which the tangent line is computed.

    Returns:
        str: A string representing the equation of the tangent line in the format 'm * x + c',
             where 'm' is the slope (rounded to 2 decimal point) and 'c' is the y-intercept
             (also rounded to 2 decimal point).

    Examples:
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x, 2)
    'x'
    >>> get_tangent(lambda x: -x, 2)
    '- x'
    >>> get_tangent(lambda x: x**2-2, 0.5)
    'x - 2.25'
    >>> get_tangent(lambda x: -x**2-2, 0.5)
    '- x - 1.75'
    >>> get_tangent(lambda x: x**2 + 5, 0)
    '5.0'
    >>> get_tangent(lambda x: x**2 - 5, 0)
    '- 5.0'
    >>> get_tangent(lambda x: x**2, 0)
    '0.0'
    >>> import math
    >>> get_tangent(math.sin, 2)
    '- 0.42 * x + 1.75'
    """
    derivative = round((func(x_0 + 10**(-5)) - func(x_0)) / (10**(-5)), 2)
    # tangent = derivative * (x-x_0) + func(x_0) = derivative * x - derivative * x_0
    a = derivative
    b = - derivative * x_0 + func(x_0)
    b = round(b, 2)
    if a == 1.0:
        a = ''
    elif a == -1.0:
        a = '- '
    elif a > 0:
        a = str(a) + " * "
    elif a < 0:
        a = "- " + str(abs(a)) + " * "
    elif a == 0:
        if b > 0:
            return str(b)
        if b < 0:
            return '- ' + str(abs(b))
        return '0.0'

    if b < 0:
        b = ' - ' + str(abs(b))
    elif b == 0:
        b = ''
    else:
        b = " + " + str(b)

    return f'{a}x{b}'



def get_root(func: callable, a: float, b: float) -> float:
    """Compute the root of a function in a given interval.

    Args:
        func (callable): The function to evaluate.
        a (float): The start of the interval.
        b (float): The end of the interval.

    Returns:
        float: The root of the function in the interval.

    Examples:
    >>> get_root(lambda x: x, -1, 1)
    0.0
    >>> get_root(lambda x: x**2 - 4, 0, 3)
    2.0
    >>> import math
    >>> get_root(math.sin, 3, 4)
    3.14
    >>> get_root(lambda x: x**2 + 1, 0, 2)
    """
    if func(a) * func(b) <= 0:
        while abs(b - a) > 10**(-5):
            midpoint = (a + b) / 2
            if func(midpoint) == 0:
                return round(midpoint,2)

            if func(a) * func(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint

        root = round(midpoint, 2)
        return root


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
