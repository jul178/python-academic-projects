"""
Game with ukrainian words - a word search game using letters from the game grid.

The player must find as many words as possible using
letters from a grid of 5 letters. Each word must contain the first and the last letter.
"""
import random

def generate_grid() -> list[list[str]]:
    """
    Generates a grid of 5 lowercasecase letters for the game.

    Returns:
        list[list[str]]: A list of 5 lowercasecase letters.
    Example: ['ґ', 'ь', 'й', 'є', 'ї']

    Examples:
    >>> grid = generate_grid()
    >>> len(grid)
    5
    >>> len(grid) == 3
    False
    """
    alphabet = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и",
                 "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с",
                 "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
    grid = random.sample(alphabet, k = 5)
    return grid

# print(generate_grid())

# 'noun', 'verb', 'adjective', 'adverb'
def choose_lanuage_part() -> str:
    """Choose a lanuage part from 'noun', 'verb', 'adjective', 'adverb'.

    Returns:
        str: A string of chosen lanuage part.
    Example: 'verb'

    Examples:
    >>> lanuage_part = choose_lanuage_part()
    """
    lanuage_parts = ['noun', 'verb', 'adjective', 'adverb']
    lanuage_part = random.choice(lanuage_parts)
    return lanuage_part

# print(choose_lanuage_part())

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


def convert_lang_part(lang_part: str) -> str:
    """
    Converts a raw part-of-speech string (PoS) into its full form.

    Args:
        lang_part (str): The raw string representing the part of speech.
    Returns:
        str: The normalized full name ('noun', 'verb', 'adjective', 'adverb').
    """
    if lang_part.startswith('non'):
        return None
    if lang_part.startswith('n'):
        return 'noun'
    if lang_part.startswith('v'):
        return 'verb'
    if lang_part.startswith('adj'):
        return 'adjective'
    if lang_part.startswith('adv'):
        return 'adverb'
    return None

def get_words(f: str, letters: list[str]) -> list[tuple[str, str]]:
    """
    Reads the dictionary file and returns words that match the game rules.

    Word selection rules:
    1. Word must contain not more than 5 letters
    2. Each word must contain the first and the last letter.
    3. Words are returned in lowercase

    Args:
        f (str): Path to the dictionary file
        letters (list[str]): List of 5 letters from the game grid in lowercase.
                             Example: ['ґ', 'ь', 'й', 'є', 'ї']

    Returns:
        list[tuple[str, str]: List of tuples of words and language part that match all rules.
    Examples:
    >>> get_words('base.lst', ['ґ', 'ь', 'й', 'є', 'ї'])
    [('ґалій', 'noun'), ('ґедзь', 'noun'), ('ґлей', 'noun'), ('ґудзь', 'noun'), ('єврей', 'noun'), \
('єлей', 'noun'), ('ємний', 'adjective'), ('єресь', 'noun'), ('їдець', 'noun'), \
('їдкий', 'adjective'), ('їнь', 'noun'), ('їхній', 'adjective'), ('йодль', 'noun')]
    """
    if isinstance(letters, list) and len(letters) == 5:
        dict_of_words = []
        with open(f, 'r', encoding='utf-8') as file:
            for line in file:
                # line_without_comment = line.split('#')[0]
                # cleaned_line = line_without_comment.rstrip(' \\')
                # # normalized_line = cleaned_line.strip().replace('/', '')
                # parts = cleaned_line.split('/')

                # if len(parts) == 2:
                #     word = parts[0].strip()
                #     lang_part = parts[1].strip()

                #     lang_part = lang_part.split()[0]
                # elif len(parts) == 1: # абразивно adv
                #     sub_parts = cleaned_line.rsplit(maxsplit=1)

                #     if len(sub_parts) != 2:
                #         continue

                #     word = sub_parts[0].strip()
                #     lang_part = sub_parts[1].strip()
                # else:
                #     continue


                # абсолютизований /adj :&&adjp:pasv:imperf:perf   # :past:pres
                # абсолютний /adj.adv \
                #'їнь noun:n:nv:np'
                line = line.strip().split(' :', maxsplit=1)[0]
                line = line.split(' #', maxsplit=1)[0]
                line = line.rstrip(' \\')
                line = line.rstrip('<')
                line = line.replace('/', '')

                parts = line.split(' ')
                if len(parts) < 2:
                    continue

                word = parts[0].strip()
                lang_part = parts[1].strip()

                # word, lang_part = parts

                if len(word) <= 5 and word[0] in letters and word[-1] in letters:
                    full_lang_part = convert_lang_part(lang_part)

                    if (full_lang_part not in ['noun', 'verb', 'adjective', 'adverb']):
                        continue

                    dict_of_words.append((word, full_lang_part))
        return dict_of_words

    return None

# print(get_words("base.lst", ['й', 'ц', 'з', 'ь', 'ш']))

# def convert_lang_part(lang_part: str) -> str:
#     """
#     Converts a raw part-of-speech string (PoS) into its full form.

#     Args:
#         lang_part (str): The raw string representing the part of speech.
#     Returns:
#         str: The normalized full name ('noun', 'verb', 'adjective', 'adverb').
#     """
#     if lang_part.startswith('n'):
#         return 'noun'
#     if lang_part.startswith('v'):
#         return 'verb'
#     if lang_part.startswith('adj'):
#         return 'adjective'
#     if lang_part.startswith('adv'):
#         return 'adverb'
#     return None


# print(convert_lang_part('n20.a.p'))


def check_user_words(user_words: list[str], language_part: str, letters: list[str],
                      vocabulary: str) -> tuple[list[str], list[str]]:
    """
    Checks user words against game rules, specified part of
    lanuage and dictionary validity.

    The function validates words from both the dictionary and the user's input
    based on the following criteria:
    1. The word must belong to the specified part of speech (`language_part`).
    2. The word must consist only of the allowed letters (`letters`).

    Returns a list of words the user correctly guessed and a list of valid
    words the user missed (words found in the dictionary but not entered by the user).

    Args:
        user_words (list[str]): A list of words entered by the user.
        language_part (str): The required part of speech that the target
                             words must match (e.g., 'noun', 'verb').
        letters (list[str]): List of 5 letters from the game grid in lowercase.
        vocabulary (str): The path to the dictionary file.
    Returns:
        tuple[list[str], list[str]]: A tuple containing two lists:
            - **List of correct words entered by the user** (words from
              `user_words` that match all rules and are found in the dictionary).
            - **List of words missed by the user** (words that match the rules
              and are in the dictionary but were not entered by the user).
    Examples:
    >>> check_user_words(['єресь', 'їхній', 'ґай'], 'noun', ['ґ', 'ь', 'й', 'є', 'ї'], 'base.lst')
    (['єресь'], ['ґалій', 'ґедзь', 'ґлей', 'ґудзь', 'єврей', 'єлей', 'їдець', 'їнь', 'йодль'])
    """
    if (isinstance(user_words, list) and isinstance(letters, list) and
        isinstance(language_part, str) and len(letters) == 5):

        dict_of_words = []

        full_lang_part = convert_lang_part(language_part)

        # if full_lang_part not in ['noun', 'verb', 'adjective', 'adverb']:
        #     terutn None


        with open(vocabulary, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().split(' :', maxsplit=1)[0]
                line = line.rstrip(' \\')
                line = line.replace('/', '')

                parts = line.split(' ')
                if len(parts) < 2:
                    continue

                word = parts[0].strip()
                language_part = parts[1].strip()

                # lang_part = language_part
                dict_lang_part = convert_lang_part(language_part)

                if dict_lang_part not in ['noun', 'verb', 'adjective', 'adverb']:
                    continue
                if dict_lang_part != full_lang_part:
                    continue

                # dict_of_words = get_words(f, letters)
                # dict_of_words = []

                if len(word) <= 5 and word[0] in letters and word[-1] in letters:
                    dict_of_words.append(word)

        correct_words = []
        misses_words = []
        for word in user_words:
            word = word.strip().lower()

            if word in dict_of_words :
                correct_words.append(word)

        for word in dict_of_words:
            if word not in user_words:
                misses_words.append(word)

        return correct_words, misses_words

    return None


def main():
    """
    Main function of the Game with ukrainian words.

    Implements the complete game scenario:
    1. Generates and displays a game grid
    2. Displays a language_part
    3. Displays a prompt and reads words from the player
    4. Gets all possible words from the dictionary
    5. Displays the number of correct words from the user
    6. Displays the correct words
    7. Displays words that the player missed
    """
    print('Починаймо гру!')
    letters = generate_grid()

    print(f"Придумай якомога більше слів, що мають не більше 5 літер та починаються і \
закінчуються на одну з наступних літер:\n{letters}")

    language_part = choose_lanuage_part()
    print(f"А ще ці слова мають бути наступною частиною мови:\n{language_part}")

    print("Твій список слів:")
    user_words = get_user_words()
    vocabulary = 'base.lst'
    # dict_of_words = get_words('base.lst', letters)
    correct_words = check_user_words(user_words, language_part, letters, vocabulary)[0]
    misses_words = check_user_words(user_words, language_part, letters, vocabulary)[1]

    print(f"Правильно запропоновані слова:\n{correct_words}")

    print(f"Пропущені слова:\n{misses_words}")


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    main()
