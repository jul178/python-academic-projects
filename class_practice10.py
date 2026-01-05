# def do_action(action, arg1, arg2):
#     return action(arg1, arg2)

# print(do_action(pow, 2.5, 2))
# print(do_action(round, 2.575, 2))
# print(do_action(pow, 2.575, 2))

# print([n  for n in range(10) if n%2 == 1])
# def is_odd(num):
#     return num%2 == 1

# print(is_odd(1))
# print(is_odd(5))
# print(is_odd(6))

# print([n for n in range(10) if is_odd(n)])
# print([is_odd(n) for n in range(10)])

# print(list(filter(is_odd, range(10))))

# def square(n):
#     return n ** 2
# print(list(map(square, range(10))))

# print(list(map(square, filter(is_odd, range(10)))))
# # /////////
# print(list(map(lambda num: num**2, range(10))))

# print(list(filter(lambda num: num%2 == 1, range(10))))
# # ////////
print(list(map(lambda num: num**2, filter(lambda num: num%2 == 1, range(10)))))
# # те саме що
print([n**2 for n in range(10) if n%2 == 1])

# words = ['...***...', '.****...', '']
# word_count = [(w, w.count('*')) for w in words]
# print(word_count)

# print(sorted(word_count))
# print(sorted(word_count, reverse=True))
# sorted_list = sorted(word_count, key=lambda word_count: word_count[1], reverse=True)
# print(sorted_list)
# print(dict(sorted_list))

# w2 = ['abc', 'a', 'ab']
# print(sorted(w2, key=lambda w: len(w)))
