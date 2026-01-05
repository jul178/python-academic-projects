"""Aliens and IQ"""
def read_file(file_path):
    """Read file and return info.

    Args:
        file_path: str: A path to the file.

    Returns:
        dict[str: int]: Dictionary where the key is name
                        of the smartest people and the value is their IQ level.
    >>> read_file('smart_people.txt')
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186, \
'Judith Polgar': 170, 'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
'Emma Watson': 132, 'Barack Obama': 137}
    """
    info = {}
    with open(file_path, 'r', encoding="utf-8") as file:
        file.readline()
        for line in file:
            parts = line.split(',')
            name = parts[0].strip()
            iq_str = parts[1].strip()
            iq = int(iq_str)
            info[name] = iq
    return info


def rescue_people(smarties, limit_iq):
    """Plan evacuation trips for smart people given an IQ limit per trip.

    Args:
        smarties(dict): Result of read_file(). Dictionary where the key is name
                        of the smartest people and the value is their IQ level.
        limit_iq(int): The maximum total IQ level of people who can be on board.

    Returns:
        tuple[int, list]: A tuple where first element is the number of needed journeys
                            and the second elements is the list of lists of journey
                            and include names of smart people that are transporting
                            in the order of aliens choise.
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": 195,
    ...                 "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    """
    sorted_smarties = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))

    journeys = []
    while sorted_smarties:
        name, iq = sorted_smarties.pop(0)
        rest = limit_iq - iq
        journey = [name]
        next_journey = []
        for name, iq in sorted_smarties:
            if iq <= rest:
                journey.append(name)
                rest -= iq
            else:
                next_journey.append((name, iq))
        sorted_smarties = next_journey
        journeys.append(journey)

    return (len(journeys), journeys)


if __name__ == '__main__':
    print(read_file('smart_people.txt'))
    print(rescue_people(read_file('smart_people.txt'), 500))
    import doctest
    print(doctest.testmod())
