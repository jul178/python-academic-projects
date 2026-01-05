"""Analyzes baby name statistics for the Lviv region (2017) using search and sort algorithms."""
def find_names(file_path) -> tuple[{str}, (int, {str}), (str, int, int)]:
    """Read file, analyse names and return a tuple of different info.

    Args:
        file_path: str: A path to the file.

    Returns:
        tuple[{str}, (int, {str}), (str, int, int)]: A tuple with three elements, where:
            The first element is the set of the three most popular names.
            The second element is a tuple,
                where the first element is the number of names that occur only once,
                and the second is the set of those names.
            The third element is a tuple,
                where the first element is the letter that most different names begin with,
                the second is the number of such names, and the third element is the number
                of children with those names.
    """
    all_names = {}
    with open(file_path, 'r', encoding="utf-8") as file:
        file.readline()
        for line in file:
            parts = line.split('\t', 1)
            name = parts[0].strip()
            freq = parts[1].strip("()\n")
            freq = int(freq)
            all_names[name] = freq

    # three_most_freq = sorted(all_names.items(), key=lambda x: x[1], reverse=True)[:3]
    list_all_names = list(all_names.items())
    def insertion_sort(lst):
        for i in range(1, len(lst)):
            temp = lst[i]
            j = i - 1
            while j >= 0 and lst[j][1] < temp[1]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = temp
        return lst

    sorted_all_names = insertion_sort(list_all_names)

    three_most_freq = set(name for name, _ in sorted_all_names[:3])

    # unique_name = {name for name, freq in all_names.items() if freq == 1}

    def linear_search(dictionary, value):
        found_keys = set()
        for key, val in dictionary.items():
            if val == value:
                found_keys.add(key)
        return found_keys

    unique_name = linear_search(all_names, 1)

    dict_letter = {}
    for name in all_names:
        first_letter = name[0]
        if first_letter not in dict_letter:
            dict_letter[first_letter] = set()
        dict_letter[first_letter].add(name)

    letter = max(dict_letter.items(), key=lambda x: len(x[1]))[0]
    names_startswith_letter = dict_letter[letter]
    count_names = len(names_startswith_letter)
    count_kids = sum(all_names[name] for name in names_startswith_letter)

    return ((three_most_freq, (len(unique_name), unique_name),
            (letter, count_names, count_kids)))



if __name__ == '__main__':
    # print(find_names('girl_names.txt'))
    print(find_names('boy_names.txt'))
    # import doctest
    # print(doctest.testmod())

