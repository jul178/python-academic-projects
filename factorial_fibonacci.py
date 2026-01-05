# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     return n * factorial_recursive(n - 1)


# def factorial_iterative( n ):



def fibonacci_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
print(fibonacci_recursive(6))

def fibonacci_iterative(n):
    a, b = 0, 1
    while a < n:
        yield a
        yield b
        a, b = b, a+b






def count_down(n):
    if n < 0:
        return 0
    print(n)
    return count_down(n - 1)
print(count_down(7))

def recursive_reverse(s):
    if len(s) <= 1:  # Base case: empty or single-character string
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]  # Recursive step

def sum_digits(n):
    if 1 <= n <= 9:
        return n
    n_str = str(n)
    return int(n_str[-1]) + sum_digits(n // 10)

text = "hello"
result = recursive_reverse(text)
print(result)
# Output: olleh





# def time_test(function, verbose=False):
