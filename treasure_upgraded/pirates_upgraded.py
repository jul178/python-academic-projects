def read_file(pathname):
    """
    Read map from a file with pathname.
    Return list of tuples, where the first element
    is direction and the second is the number of steps.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete=False) as tmpfile:
    ...     _ = tmpfile.write('U 2\\nR 2\\nD 2\\nL 2')
    >>> with open(tmpfile.name, 'r', encoding='utf-8') as file:
    ...    print(file.read())
    U 2
    R 2
    D 2
    L 2
    >>> read_file(tmpfile.name)
    [('U', 2), ('R', 2), ('D', 2), ('L', 2)]
    >>> read_file("treasure.txt")
    [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        # content = file.readlines()
        result = []
        # for line in content:
        for line in file:
            direct, n_steps = line.strip().split()
            result.append((direct, int(n_steps)))
    return result

def find_path(treasure_map: list[tuple[str, int]]) -> list[tuple[int, int]]:
    """
    Finds the path in coordinates according to treasure_map
    assuming that start is in (0, 0).
    If we go left by 1 from the start, the coordinate is (0, -1).
    If right – (0, 1).
    If we go up by 1 from the start, the coordinate is (-1, 0).
    If down – (1, 0).
    Return the list of coordinates.

    :param treasure_map: list[tuple[str, int]], A list of tuples, where each tuple
                                is (Direction string, Number of steps integer).
    :return: tist[tuple[int, int]], A list of tuples, where each tuple
                                is (x-coordinate, y-coordinate).
    >>> find_path([('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), \
                     ('L', 11), ('D', 7), ('R', 7), ('U', 3)])
    [(0, 0), (-1, 0), (-2, 0), (-2, 1), (-2, 2), \
(-1, 2), (0, 2), (0, 3), (0, 4), (-1, 4), (-2, 4), \
(-3, 4), (-4, 4), (-4, 3), (-4, 2), (-4, 1), (-4, 0), \
(-4, -1), (-4, -2), (-4, -3), (-4, -4), (-4, -5), \
(-4, -6), (-4, -7), (-3, -7), (-2, -7), (-1, -7), \
(0, -7), (1, -7), (2, -7), (3, -7), (3, -6), \
(3, -5), (3, -4), (3, -3), (3, -2), (3, -1), \
(3, 0), (2, 0), (1, 0), (0, 0)]
    """
    x, y = 0, 0
    path = [(x, y)]

    for direction, steps in treasure_map:
        match direction:
            case 'U':
                for _ in range(steps):
                    x -= 1
                    path.append((x, y))
            case 'D':
                for _ in range(steps):
                    x += 1
                    path.append((x, y))
            case 'R':
                for _ in range(steps):
                    y += 1
                    path.append((x, y))
            case 'L':
                for _ in range(steps):
                    y -= 1
                    path.append((x, y))
            case _:
                return None
    return path

        # if direction == 'U':
        #     move_up = x - steps
        #     path.append(move_up)
        # elif direction == 'D':
        #     move_down = x + steps
        #     path.append(move_down)
        # elif direction == 'R':
        #     move_right = y + steps
        #     path.append(move_right)
        # elif direction == 'L':
        #     move_left = y - steps
        #     path.append(move_left)
# print(find_path([('U', 2), ('R', 2), ('R', 2), ('D', 2), ('L', 4)]))

def find_positive_path(path):
    '''Find the path with nonnegative coordinates by shifting
    the path horizontally and vertically by minimal steps.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), \
                        ('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> path = find_path(treasure_map)
    >>> find_positive_path(path)
    [(4, 7), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), \
(4, 9), (4, 10), (4, 11), (3, 11), (2, 11), (1, 11), \
(0, 11), (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (0, 5), \
(0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), \
(3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), \
(7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (6, 7), (5, 7), (4, 7)]
    '''
    positive_path = []
    min_x = min(x for x, y in path)
    min_y = min(y for x, y in path)

    # min_x, min_y = path[0]
    # for x, y in path[1:]:
    #     min_x = min(min_x, x)
    #     min_y = min(min_y, y)

    for x, y in path:
        # min_x = min(x)
        # min_y = min(y)
        non_neg_x = x + abs(min_x)
        non_neg_y = y + abs(min_y)
        positive_path.append((non_neg_x, non_neg_y))
    return positive_path



def find_size(path: list[tuple[int, int]]) -> tuple[int, int]:
    '''Finds the size of the map: minimal number of points vertically
    and horizontally needed to build the path. Return tuple where the
    first coordinate is the height of the map and the second is the length.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), \
                        ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> find_size(find_positive_path(find_path(treasure_map)))
    (8, 12)
    '''
    max_x = max(x for x, y in path)
    max_y = max(y for x, y in path)
    size = tuple((max_x + 1, max_y + 1))
    return size

def view_map(path: list[tuple[int, int]]) -> str:
    '''
    From path creates the map. Returns string representation of the map.
    If the coordinate is on the path, put the symbol 'x'.
    Otherwise use '.'.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), \
                        ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> path = find_path(treasure_map)
    >>> view_map(path)
    'xxxxxxxxxxxx\\n\
x..........x\\n\
x......xxx.x\\n\
x......x.x.x\\n\
x......x.xxx\\n\
x......x....\\n\
x......x....\\n\
xxxxxxxx....'
    '''
    # size,
    # lenght = size[0]
    # width = size[1]
    # area = lenght * width

    # if len(str_map) == width:
    #     str_map = "." * area
    # return str_map

    # str_map = ''
    # while len(str_map) <= area:
    #     if len(str_map) % width == 0:
    #         str_map += "." + "\n"
    #     else:
    #         str_map += "."
    # return str_map
    max_x, max_y = find_size(find_positive_path(path))
    positive_path = find_positive_path(path)
    rows = max_x
    columns = max_y
    matrix = []
    for row in range(rows):
        current_row = []
        for _ in range(columns):
            current_row.append('.')

        matrix.append(current_row)

    for x, y in positive_path:
        matrix[x][y] = 'x'

    output_rows = []
    for row in matrix:
        str_row = ''.join(row)
        output_rows.append(str_row)

    return '\n'.join(output_rows)


def find_vertices(treasure_map: list[tuple[str, int]]) -> list[tuple[int, int]]:
    '''Find the vertices of polygon that created on our map.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
                         ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> find_vertices(treasure_map)
    [(-2, 0), (-2, 2), (0, 2), (0, 4), (-4, 4), (-4, -7), (3, -7), (3, 0)]
    >>> treasure_map = [('U', 2), ('R', 2), ('R', 2), ('D', 2), ('L', 4)]
    >>> find_vertices(treasure_map)
    [(0, 0), (-2, 0), (-2, 4), (0, 4)]
    '''
    vertices = []
    path = find_path(treasure_map)
    # max_steps = max(steps for direction, steps in treasure_map)
    # for direction, steps in treasure_map:
    #     if steps == max_steps:
    #         vertices.append(path[current_index])
    #     current_index += steps
        # else:
        #     continue
    dx_prev = path[1][0] - path[0][0]
    dy_prev = path[1][1] - path[0][1]

    for i in range(1, len(path) - 1):

        dx_curr = path[i + 1][0] - path[i][0]
        dy_curr = path[i + 1][1] - path[i][1]

        if (dx_prev, dy_prev) != (dx_curr, dy_curr):
            vertices.append(path[i])

        dx_prev, dy_prev = dx_curr, dy_curr

    first_dx = path[1][0] - path[0][0]
    first_dy = path[1][1] - path[0][1]
    last_dx = path[-1][0] - path[-2][0]
    last_dy = path[-1][1] - path[-2][1]

    if (first_dx, first_dy) != (last_dx, last_dy):
        vertices.insert(0, (0, 0))

    return vertices


def calculate_polygon_area(vertices: list[tuple[int, int]]) -> int:
    '''
    Calculate the polygon area using the list of vertices of the
    polygon.
    >>> vertices = find_vertices([('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
                                   ('L', 11), ('D', 7), ('R', 7), ('U', 3)])
    >>> calculate_polygon_area(vertices)
    61
    '''
    area = 0
    for i, (x_1, y_1) in enumerate(vertices):
        x_n, y_n = vertices[(i + 1) % len(vertices)]
        area += x_1 * y_n - x_n * y_1
    return abs(area) // 2

def find_volume_treasure(area: int, length: int) -> int:
    '''
    Find the number of interior points. Each point is one treasure.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
                         ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> vertices = find_vertices(treasure_map)
    >>> area = calculate_polygon_area(vertices)
    >>> length = len(find_path(treasure_map))-1
    >>> find_volume_treasure(area, length)
    42
    '''
    # Area = i + length / 2 - 1
    interior_points = area - length/2 + 1
    return int(interior_points)

def write_map_to_file(mapa, pathname):
    '''
    Write the mapa to the file with path pathname.
    Returns nothing.

    >>> mapa = 'xxx\\nx.x\\nxxx'
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w+', delete=False) as tmpfile:
    ...    write_map_to_file(mapa, tmpfile.name)
    ...    print(tmpfile.read())
    xxx
    x.x
    xxx
    '''
    with open(pathname, 'w', encoding='utf-8') as file:
        file.write(mapa)



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    write_map_to_file(view_map(find_path(read_file('treasure.txt'))), 'treasure_map.txt')
