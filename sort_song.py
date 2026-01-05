"""Sorts songs by the specified parameter (key)"""
from typing import Callable


def song_length(x: tuple[str, str]) -> float:
    '''Returns the length of the song as a float,
    used for sorting by song length.

    Parameters:
    song (tuple[str, str]): A tuple containing the song title
    and its length as a string.

    Returns:
    float: The length of the song converted to a float.

    >>> song_length(('Янанебібув', '3.19'))
    3.19
    '''
    _, length = x
    if isinstance(length, str):
        return float(length)
    return None


def title_length(x: tuple[str]) -> int:
    '''Returns the length of the song title,
    used for sorting by title length.

    Parameters:
    song (tuple[str, str]): A tuple containing the song title
    and its length.

    Returns:
    int: The length of the song title.

    >>> title_length(('Сосни', '4.31'))
    5
    '''
    title, _ = x
    if isinstance(title, str):
        return len(title)
    return None



def last_word(x: tuple[str]) -> str:
    """
    Returns the first letter of the last word of the song title,
    used for sorting by last word.

    Parameters:
    song (tuple[str, str]): A tuple containing the song title and its length.

    Returns:
    str: The first letter of the last word in the song title.

    >>> last_word(('Той день', '3.58'))
    'д'
    """
    title, _ = x

    if isinstance(title, str):
        words = title.split()
        last = words[-1]
        first_letter = last[0]

        return first_letter
    return None

def sort_songs(
        song_titles: list[str],
        length_songs: list[str],
        key: Callable[[tuple], int | str | float]) -> list[tuple] | None:
    '''Sorts songs based on the specified key.

    Parameters:
    song_titles (list[str]): A list of song titles.
    length_songs (list[str]): A corresponding list of song lengths.
    key (Callable): The key by which to sort (song_length, title_length, last_word).

    Returns:
    list[tuple[str, str]]]: A sorted list of tuples (song title, song length)
    or None if input is invalid.

    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни'],\
                   ['3.19', '3.58', '5.06', '4.31'],  song_length)
    [('Янанебібув', '3.19'), ('Той день', '3.58'), ('Сосни', '4.31'), ('Мало мені', '5.06')]
    '''
    if isinstance(song_titles, list) and isinstance(length_songs, list):

        if len(song_titles) == len(length_songs):
            songs = list(zip(song_titles, length_songs))
            songs.sort(key=key)

            return songs
        return None
    
    return None

# titles = ['Янанебібув', 'Той день', 'Мало мені', 'Сосни']
# lengths = ['3.19', '3.58', '5.06', '4.31']
# print(sort_songs(titles, lengths, title_length))

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
