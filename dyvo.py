""" A module for string manipulations.
Provides the `insert_dyvo` function to add the word "dyvo"
before every word in a sentence that begins with a
specified flag (substring).
"""
def insert_dyvo(sentence: str, flag: str) -> str | None:
    """
    Insert word "диво" before every word in the sentence that starts with the flag.

    param sentence: str, The input sentence to modify.
    param flag: str, The substring to check for at the start of each word.
    return: str or None, The modified sentence with inserted word "dyvo",
                    or None if the input `sentence` or `flag` is not a string.
    >>> insert_dyvo('Кит кота по хвилях катав - кит у воді, кіт на киті', 'ки')
    'Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    >>> insert_dyvo('Абзац починався зі слів: Абрикоси ростуть влітку', 'аб')
    'Дивоабзац починався зі слів: Дивоабрикоси ростуть влітку'
    >>> insert_dyvo(123, '1')
    """
    if isinstance(sentence, str) and isinstance(flag, str):
        words = sentence.split()
        result = words.copy()

        flag_low = flag.lower()

        for i, word in enumerate(words):
            word_low = word.lower()

            if word_low.startswith(flag_low):

                if word[0].isupper():

                    result[i] = 'Диво' + word_low
                    # word = word.lower()
                # if i == 0:
                #     result[i] = 'Диво' + word_low
                else:
                    result[i] = 'диво' + word_low

        return ' '.join(result)
    return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
