"""Graph operations"""
def get_graph_from_file(filename: str) -> list[list[int]]:
    """
    Reads a graph from a specified file and returns a list of edges.
    The file should contain pairs of integers representing edges,
    with each edge formatted as "node1,node2" on a new line.
    For example:
        1,2
        3,4
        1,5

    Parameters:
    -----------
    filename: str
        The path to the file containing the graph edges in comma-separated format.

    Returns:
    --------
    list[list[int]]:
        A list of edges, where each edge is represented as a list of two integers.

    Example:
    --------
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(filename, 'r', encoding='utf-8') as file:
        result = []
        for line in file:
            node1, node2 = line.strip().split(',')
            result.append([int(node1), int(node2)])
    return result


def to_edge_dict(edge_list: list[list[int]]) -> dict[int, list[int]]:
    """
    Converts a graph from a list of edges to a dictionary representation.
    Each node maps to a list of adjacent nodes based on the edges provided.
    The list of nodes should be sorted in ascending order.

    Parameters:
    -----------
    edge_list : list[list[int]]
        A list of edges, where each edge is represented as a list of two integers.

    Returns:
    --------
    dict[int, list[int]]:
        A dictionary with nodes as keys and lists of adjacent nodes as values.

    Example:
    --------
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    d = {}
    for pair in edge_list:
        el1, el2 = pair
        if el1 not in d:
            d[el1] = []
        if el2 not in d:
            d[el2] = []
        if el2 not in d[el1]:
            d[el1].append(el2)
        if el1 not in d[el2]:
            d[el2].append(el1)
    for val_list in d.values():
        val_list.sort()
    return d



def is_edge_in_graph(graph:  dict[int, list[int]], edge: tuple[int, int]) -> bool:
    """
    Checks if a given edge exists in the graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to check.

    Returns:
    --------
    bool:
        True if the edge exists in the graph; False otherwise.

    Example:
    --------
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    ed1, ed2 = edge
    if ed1 in graph and ed2 in graph[ed1]:
        return True
    if ed2 in graph and ed1 in graph[ed2]:
        return True
    return False


def add_edge(graph: dict[int, list[int]], edge: tuple[int, int]) -> dict[int, list[int]]:
    """
    Adds a new edge to the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to add.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the new edge included.

    Example:
    --------
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    ed1, ed2 = edge
    # if ed1 not in graph and ed2 not in graph[ed1]:
    #     graph[key].update(ed1)
    # elif ed2 not in graph and ed1 not in graph[ed2]:
    #     graph[key].update(ed2)
    if ed1 not in graph:
        graph[ed1] = [ed2]
    elif ed2 not in graph[ed1]:
        graph[ed1].append(ed2)
    if ed2 not in graph:
        graph[ed2] = [ed1]
    elif ed1 not in graph[ed2]:
        graph[ed2].append(ed1)
    return graph


def del_edge(graph: dict[int, list[int]], edge: tuple[int, int]) -> dict[int, list[int]]:
    """
    Removes an edge from the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to remove.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the specified edge removed.

    Example:
    --------
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    ed1, ed2 = edge
    if ed1 in graph and ed2 in graph[ed1]:
        graph[ed1].remove(ed2)
    if ed2 in graph and ed1 in graph[ed2]:
        graph[ed2].remove(ed1)
    return graph


def add_node(graph: dict[int, list[int]], node: int) -> dict[int, list[int]]:
    """
    Adds a new node to the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    node : int
        The node to add to the graph.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the new node included.

    Example:
    --------
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph:
        graph[node] = []
    return graph

def del_node(graph: dict[int, list[int]], node: int) -> dict[int, list[int]]:
    """
    Deletes a node and all its incident edges from the graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    node : int
        The node to delete from the graph.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the specified node and its edges removed.

    Example:
    --------
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph:
        for el in graph[node]:
            if el in graph and node in graph[el]:
                graph[el].remove(node)
        graph.pop(node)
    return graph


def convert_to_dot(filename: str) -> None:
    """
    Reads a file of edges, converts it into a directed graph in DOT format,
    and saves it as a file with the same name but with a .dot extension.

    This function allows for quick visualization and verification of
    graph functions by exporting them in a format that can be rendered as a graph.

    Parameters:
    -----------
    filename : str
        The name of the input file containing graph edges in "node1,node2" format,
        with one edge per line.

    Returns:
    --------
    None
        Saves the directed graph in DOT format to a file with the same
        name as the input file but with a .dot extension.

    Example:
    --------
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode= 'w+', suffix=".txt") as temp_input:
    ...     _ = temp_input.write("1,2\\n3,4\\n1,5\\n")
    ...     _ = temp_input.seek(0)
    ...     convert_to_dot(temp_input.name)
    ...     output_file = temp_input.name.replace('.txt', '.dot')
    ...     with open(output_file, 'r') as temp_output:
    ...         print(temp_output.read())
    digraph {
    1 -> 2
    1 -> 5
    2 -> 1
    3 -> 4
    4 -> 3
    5 -> 1
    }
    """
    edges = set()
    # with open(filename, 'r+', encoding='utf-8') as file:
    #     for line in file:
    #         line = line.strip()
    #         node1, node2 = line.strip().split(',')
    #         n1, n2 = int(node1), int(node2)
    #         if n1 < n2:
    #             edges.add((n1, n2))
    #         elif n2 < n1:
    #             edges.add((n2, n1))
    graph = get_graph_from_file(filename)

    for pair in graph:
        n1, n2 = pair
        edges.add((n1, n2))
        edges.add((n2, n1))
            # else:
            #     continue
    # reverse = []
    # for n1, n2 in sorted(edges):
    #     reverse.append((n2, n1))

    dot = "digraph {\n"
    for n1, n2 in sorted(edges):
        dot += (f"{n1} -> {n2}\n")
    # for n1, n2 in sorted(edges):
    #     dot += (f"{n2} -> {n1}\n")
    dot += "}"

    parts = filename.split('.')
    n_parts = parts[:-1]
    name = ''.join(n_parts)
    output_filename = name + ".dot"

    with open(output_filename, 'w', encoding='utf-8') as file_out:
        file_out.write(dot)

if __name__ == '__main__':
    
    import doctest
    print(doctest.testmod())
