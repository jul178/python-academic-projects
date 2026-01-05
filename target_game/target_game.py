"""
Target Game - a word search game using letters from the game grid.

The player must find as many words as possible (minimum 4 letters) using
letters from a 3x3 grid. Each word must contain the central letter.
"""
import random

def generate_grid() -> list[list[str]]:
    """
    Generates a 3x3 grid of uppercase letters for the game.

    The grid should contain 3 vowels and 6 consonants for optimal game
    balance.

    Returns:
        list[list[str]]: A list of 3 lists, each containing 3 uppercase letters.
    Example: [['E', 'T', 'O'], ['O', 'P', 'N'], ['P', 'U', 'R']]

    Examples:
    >>> grid = generate_grid()
    >>> len(grid)
    3
    >>> all(len(row) == 3 for row in grid)
    True
    >>> len([letter for row in grid for letter in row])
    9
    """
    vovels = ['A', 'E', 'I', 'O', 'U', 'Y']
    chosen_vovels = random.choices(vovels, k=3)
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
                  'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    chosen_consonants = random.choices(consonants, k=6)
    letters = chosen_vovels + chosen_consonants
    random.shuffle(letters)
    # print(letters)

    grid = []
    for i in range(0, 9, 3):
        row = letters[i:i+3]
        grid.append(row)
    return grid

# print(generate_grid())


def get_words(pathname: str, letters: list[str]) -> list[str]:
    """
    Reads the dictionary file and returns words that match the game rules.

    Word selection rules:
    1. Word must contain at least 4 letters
    2. Word must contain the central letter
    3. Each letter in the word is used no more times than it appears on the grid
    4. All letters in the word must be present on the grid
    5. Words are returned in lowercase

    Args:
        pathname (str): Path to the dictionary file
        letters (list[str]): List of 9 letters from the game grid in lowercase.
                             Element at index 4 is the central letter (mandatory).
                             Example: ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r']

    Returns:
        list[str]: List of words from the dictionary that match all rules.

    Examples:
        >>> get_words("en.txt", ['w', 'u', 'm', 'r', 'o', 'v', 'k', 'i', 'f'])
        ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', 'komi', 'kori', \
'miro', 'moki', 'ovum', 'work', 'worm', 'wouf']
        >>> words = get_words("en.txt", ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r'])
        >>> all('p' in word for word in words)
        True
        >>> all(len(word) >= 4 for word in words)
        True
    """
    if isinstance(letters, list) and len(letters) == 9:
        result = []
        # try:
        with open(pathname, 'r', encoding='utf-8') as file:
            for word in file:
                word = word.strip().lower()

                if len(word) < 4 or letters[4] not in word:
                    continue

                valid = True
                for letter in word:
                    if letter not in letters or word.count(letter) > letters.count(letter):
                        valid = False
                        break
                    # continue
                if valid and word not in result:
                    result.append(word)
        return result

        # except FileNotFoundError:
        #     return []

    return None

# letters = ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i']
# words = get_words("en.txt", letters)
# print(words[:20])

def get_user_words() -> list[str]:
    """
    Reads words from user input until EOF signal is received.

    The user enters one word per line. Input is terminated by pressing:
    - Unix/Linux/Mac: Ctrl+D
    - Windows: Ctrl+Z, then Enter

    Returns:
        list[str]: List of words entered by the user.

    Note:
        This function does not print any messages to the screen. All
        instructions for the user should be displayed in the main() function.
    """
    words = []
    while True:
        try:
            word = input().strip().lower()
            words.append(word)
        except EOFError:
            break
    return words


# n = int(input())
# for i in range(n):
#     print(get_user_words())

def get_pure_user_words(user_words: list[str], letters: list[str],
                         words_from_dict: list[str]) -> list[str]:
    """
    Checks user words and returns those that match game rules but are not in the dictionary.

    This function helps identify words that the user entered correctly according
    to the game rules (length >= 4, contain central letter, all letters are on
    the grid), but which were not found in the game dictionary. These could be
    spelling errors or rare words.

    Args:
        user_words (list[str]): Words entered by the user.
        letters (list[str]): List of 9 letters from the game grid (lowercase).
                             Element [4] is the central letter.
        words_from_dict (list[str]): Words from the dictionary that match the rules.

    Returns:
        list[str]: List of user words that match game rules but are not found
                   in the dictionary.

    Examples:
        >>> get_pure_user_words(['impi', 'gipm'], ['i', 'g', 'e', 'p', 'i', 's', 'w', 'm', 'g'], \
['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', \
'kori', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf'])
        ['impi', 'gipm']
        >>> get_pure_user_words(['test'], ['i', 'g', 'e', 'p', 'i', 's', 'w', 'm', 'g'], [])
        []
        >>> get_pure_user_words(['pig'], ['p', 'i', 'g', 'e', 'p', 's', 'w', 'm', 'g'], [])
        []
    """
    if (isinstance(user_words, list) and isinstance(letters, list) and
        isinstance(words_from_dict, list) and len(letters) == 9):

        out_of_dictionary = []

        for word in user_words:
            word = word.strip().lower()
            if len(word) < 4 or letters[4] not in word:
                continue

            valid = True
            for letter in word:
                if letter not in letters or word.count(letter) > letters.count(letter):
                    valid = False
                    break
                continue

            if valid and word not in words_from_dict and word not in out_of_dictionary:
                out_of_dictionary.append(word)
        return out_of_dictionary
    return None


def main():
    """
    Main function of the Target game.

    Implements the complete game scenario:
    1. Generates and displays a 3x3 game grid
    2. Displays a prompt and reads words from the player
    3. Gets all possible words from the dictionary
    4. Displays the number of correct words from the user
    5. Displays all possible words from the dictionary
    6. Displays words that the player missed
    7. Displays player's words that are not in the dictionary
    """
    grid = generate_grid()
    print(f"Your board is {grid}")

    print("Please, suggest your words here:")
    user_words = get_user_words()

    letters = []
    for row in grid:
        for letter in row:
            letters.append(letter.lower())
    words_from_dict = get_words('en.txt', letters)
    out_of_dictionary = get_pure_user_words(user_words, letters, words_from_dict)
    right_words = []
    for word in user_words:
        if word in words_from_dict :
            right_words.append(word)

    print(f"Number of right word: {len(right_words)}")
    print(f"All posible words:\n{words_from_dict}")

    misses_words = []
    for word in words_from_dict:
        if word not in user_words:
            misses_words.append(word)
    print(f"You missed the following words:\n{misses_words}")
    print(f"You suggest, but we don't have them in dictionary:\n{out_of_dictionary}")



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    main()
