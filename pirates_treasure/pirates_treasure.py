"""This module provides a set of tools for analyzing pirate treasure maps,
navigating paths, and locating hidden treasures based on intersecting paths.
It includes functions for defining direction by azimuth, reading map data from files,
calculating paths based on directional steps, determining map dimensions, shifting paths to
a normalized coordinate system, finding intersections between paths, and
visualizing the results.
"""
def define_direction(previous_direction: str, azimuth: int) -> str:
    """
    Calculate the new path direction based on the current direction
    and the pirate's biased azimuth. The azimuth is given in degrees
    and can be any non-negative multiple of 90. The directions are
    represented as 'N' for North, 'E' for East, 'S' for South, and 'W'
    for West.

    Args:
    previous_direction (str): The current direction ('N', 'E', 'S', 'W').
    azimuth (int): The azimuth in degrees (non-negative multiple of 90).

    Returns:
    str: The new direction as a single character string.

    For example:
    - If the current direction is North ('N') and the azimuth is 90 degrees,
      the new direction will be East ('E').
    - If the current direction is South ('S') and the azimuth is 90 degrees,
      the new direction will be West ('W').

    >>> define_direction('N', 0)
    'N'
    >>> define_direction('N', 90)
    'E'
    >>> define_direction('N', 180)
    'S'
    >>> define_direction('N', 270)
    'W'
    >>> define_direction('E', 90)
    'S'
    >>> define_direction('W', 270)
    'S'
    """
    if isinstance(previous_direction, str) and isinstance(azimuth, int):
        world_sides = ('N', 'E', 'S', 'W')
        sides_dict = {}

        if previous_direction in world_sides and 360 >= azimuth >= 0 and azimuth % 90 == 0:
            new_direction = ''

            for num, direct in enumerate(world_sides):
                sides_dict[direct] = num
            # print(sides_dict)

            match azimuth:
                case 0 | 360:
                    new_direction = previous_direction
                case 90:
                    new_direction = world_sides[(sides_dict[previous_direction] + 1) % 4]
                case 180:
                    new_direction = world_sides[(sides_dict[previous_direction] + 2) % 4]
                case 270:
                    new_direction = world_sides[(sides_dict[previous_direction] + 3) % 4]
                case _:
                    return None
            return new_direction
    return None

def read_map(file_name: str) -> tuple:
    """
    Reads a map from the specified file and interprets the directions
    and steps for navigation. The map file contains information about
    the starting coordinates and the steps to be taken in a specified
    direction. The initial direction is assumed to be North.

    The map file should be structured in such a way that it lists the
    starting coordinates (x, y) followed by directions (N, E, S, W)
    and the corresponding number of steps to take in each direction.

    Note: The file may contain empty lines, which should be ignored.

    Args:
    file_name (str): The pathname of the file containing the map data.

    Returns:
    tuple: A tuple containing two elements:
        - The first element is a tuple (x, y) representing the starting
          coordinates.
        - The second element is a list of tuples, where each tuple contains:
            - A direction (str): 'N' for North, 'E' for East, 'S' for South,
              or 'W' for West.
            - The number of steps (int) to take in that direction.

    >>> read_map("treasure_3.txt")
    ((0, 11), \
[('W', 5), ('W', 6), ('S', 7), ('E', 3), ('E', 4), \
('N', 5), ('E', 2), ('S', 2), ('E', 2), ('N', 4)])
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        res_list = []
        line = file.readline()
        x, y = line.strip().split()
        start_coord = (int(x), int(y))

        current_direc = 'N'
        for line in file:
            line = line.strip()
            if line:
                line = line.split()
                azimuth = line[0]
                steps = line[1]
                direction = define_direction(current_direc, int(azimuth))
                res_list.append((direction, int(steps)))
                current_direc = direction
    return (start_coord, res_list)


def find_path(start: tuple, treasure_directions: list) -> list:
    """
    Calculates the path of coordinates based on the given start position
    and a series of directional steps. The start position is provided as
    a tuple of coordinates (x, y).

    The function interprets movement based on the following directional
    rules, with steps determining how far to move in a given direction:
    - 'W' (West): decreases the y-coordinate (moves left).
    - 'E' (East): increases the y-coordinate (moves right).
    - 'N' (North): decreases the x-coordinate (moves up).
    - 'S' (South): increases the x-coordinate (moves down).

    Args:
    start (tuple): A tuple representing the starting coordinates (x, y).
    treasure_directions (list of tuple): A list of tuples where each tuple
                                         contains:
                                         - A direction ('N', 'E', 'W', 'S')
                                         - An integer representing the number
                                           of steps to take in that direction.

    Returns:
    list of tuple: A list of coordinates (x, y) representing the path taken
                   from the start position, including all intermediate steps.

    >>> start = (0, 0)
    >>> path = [('E', 3), ('S', 3), ('W', 3), ('N', 3)]
    >>> find_path(start, path)
    [(0, 0), \
(0, 1), (0, 2), (0, 3), \
(1, 3), (2, 3), (3, 3), \
(3, 2), (3, 1), (3, 0), \
(2, 0), (1, 0), (0, 0)\
]
    """
    if isinstance(start, tuple) and isinstance(treasure_directions, list):
        x, y = start
        path = [(start)]

        for direction, steps in treasure_directions:
            match direction:
                case 'N':
                    for _ in range(steps):
                        x -= 1
                        path.append((x, y))
                case 'S':
                    for _ in range(steps):
                        x += 1
                        path.append((x, y))
                case 'E':
                    for _ in range(steps):
                        y += 1
                        path.append((x, y))
                case 'W':
                    for _ in range(steps):
                        y -= 1
                        path.append((x, y))
                case _:
                    return None
        return path
    return None



def find_treasure(path1: list, path2: list) -> tuple | None:
    """
    Determines the location of the treasure based on the intersection of
    two paths. The function identifies the point of intersection and
    calculates the treasure's location based on the following conditions:

    - If the paths intersect at exactly one point, that point is the
      treasure's location.
    - If the paths intersect at exactly two points, the treasure is located
      at the midpoint between these two points. If the coordinates of the
      midpoint are fractional, they are rounded down to the nearest integer.
    - If the paths intersect at more than two points, it is impossible
      to determine the treasure's exact location, and the function
      returns `None`.

    Args:
    path1 (list of tuple): The first path, represented as
                           a list of coordinates (x, y).
    path2 (list of tuple): The second path, represented as
                           a list of coordinates (x, y).

    Returns:
    tuple or None: The coordinates (x, y) of the treasure if it
    can be determined, or `None`  if the treasure's location
    cannot be identified.

    >>> path1 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]
    >>> path2 = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> path3 = [(1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4)]
    >>> find_treasure(path1, path2)
    (2, 2)
    >>> find_treasure(path1, path3)
    (1, 2)
    >>> find_treasure(path2, path3)
    """
    if isinstance(path1, list) and isinstance(path2, list) and path1 != [] and path2 != []:
        treasure_coord = []
        path1 = path1[:-1]
        path2 = path2[:-1]
        for coord in path1:
            if coord in path2:
                treasure_coord.append((coord))

        if len(treasure_coord) == 2:
            x_midpoint = sum(x for x, y in treasure_coord) / 2
            y_midpoint = sum(y for x, y in treasure_coord) / 2
            x = int(x_midpoint)
            y = int(y_midpoint)
            return (x, y)
        if len(treasure_coord) == 1:
            return treasure_coord[0]
        return None
    return None


def find_size(path: list) -> tuple:
    """
    Calculates the size of the map based on the given path. The size of the map
    is determined by the minimal number of points needed vertically and
    horizontally to encompass the entire path. The height is the difference
    between the maximum and minimum x-coordinates, and the width is the
    difference between the maximum and minimum y-coordinates.

    Args:
    path (list of tuple): A list of coordinates (x, y) representing the path.

    Returns:
    tuple: A tuple (height, width) where:
        - height is the number of points needed vertically.
        - width is the number of points needed horizontally.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> find_size(path)
    (3, 3)
    """
    if isinstance(path, list):
        min_x = min(x for x, y in path)
        max_x = max(x for x, y in path)
        min_y = min(y for x, y in path)
        max_y = max(y for x, y in path)
        height = max_x - min_x
        lenght = max_y - min_y
        return (height + 1, lenght + 1)
    return None


def shift_path(path: list) -> tuple:
    """
    Shifts the given path to ensure that all coordinates are non-negative
    and the smallest coordinate is positioned at (0, 0).

    The function returns a tuple, where the first element is a tuple
    containing the minimum y and x values before the shift, and the second
    element is the list of shifted coordinates.

    Args:
    path (list of tuple): A list of tuples where each tuple represents a
                          coordinate (x, y) along the path.

    Returns:
    tuple: A tuple where:
        - The first element is a tuple representing the minimum
          y-coordinate and x-coordinate found in the path.
        - The second element is a list of tuples representing the shifted path,
          where all coordinates are non-negative.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> shift_path(path)
    ((2, 2), [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)])
    """
    if isinstance(path, list):
        min_x = min(x for x, y in path)
        min_y = min(y for x, y in path)
        pos_path = []
        for x, y in path:
            x -= min_x
            y -= min_y
            pos_path.append((x, y))
        return ((min_x, min_y), pos_path)
    return None


def decode_map(file_name1: str, file_name2: str, map_file_name: str):
    """
    Draws a map that visualizes two paths and the treasure (if it exists)
    based on the paths provided in two input files. The map is written
    to the specified output file.

    - The paths are marked with `.`.
    - The start of the first path is marked with `1`.
    - The start of the second path is marked with `2`.
    - If the start of the first and second path coincides, it is
      marked with `3`.
    - If the treasure is found (i.e., the paths intersect at a specific point),
      it is marked with `x`. The treasure marker `x` overwrites the start
      markers '1' and '2' if they coincide with the treasure's location.

    Args:
    file_name1 (str): The name of the file containing the first path.
    file_name2 (str): The name of the file containing the second path.
    map_file_name (str): The name of the output file where the map will be drawn.

    Returns:
    None: The map is written directly to the output file.

    >>> decode_map('treasure_1.txt', 'treasure_2.txt', 'output.txt')
    >>> with open('output.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    1..
    . .
    ..x.2
      . .
      ...
    """
    start_coord1, res_list1 = read_map(file_name1)
    path1 = find_path(start_coord1, res_list1)

    start_coord2, res_list2 = read_map(file_name2)
    path2 = find_path(start_coord2, res_list2)

    treasure_coord = find_treasure(path1, path2)
    all_coords = path1 + path2

    if not all_coords:
        return None
    (min_x, min_y), shifted_all_coords = shift_path(all_coords)

    (height, width) = find_size(shifted_all_coords)
    matrix = []
    for _ in range(height):
        current_row = []
        for _ in range(width):
            current_row.append(' ')
        matrix.append(current_row)

    for x, y in all_coords:
        x = x - min_x
        y = y - min_y
        matrix[x][y] = '.'

    x1, y1 = path1[0]
    x2, y2 = path2[0]

    x1 -= min_x
    x2 -= min_x
    y1 -= min_y
    y2 -= min_y

    if (x1, y1) == (x2, y2):
        matrix[x1][y1] = '3'
    else:
        matrix[x1][y1] = '1'
        matrix[x2][y2] = '2'

    if treasure_coord:
        x, y = treasure_coord
        x -= min_x
        y -= min_y
        matrix[x][y] = 'x'

    output_rows = []
    for row in matrix:
        output_rows.append(''.join(row))

    with open(map_file_name, 'w', encoding='utf-8') as file:
        file.write('\n'.join(output_rows))


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
