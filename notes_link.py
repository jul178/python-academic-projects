"""Builds note-link graphs from Markdown files and exports them to DOT."""
import re

def build_graph_from_note(note_path: str, graph = None) -> dict:
    """
    Builds a directed graph of connections between notes, starting from the
    given note file.

    Args:
        note_path (str): Path to the file with note, that needed to buitl a graph for.
        graph (dict): Optional, in case it needed to extend existing graph(dict).
    Returns:
        dict: Dictionary: keys are names of the notes and the values are an ordered list of \
            the names of notes which it is directly connected to(in the usual order of \
            comparison of strings). If the note is connected to nothing, then ifs keys \
            should not be in the dictionary.

    >>> build_graph_from_note("notes/note.md")
    {'note': ['note4'], 'note4': ['note']}
    >>> build_graph_from_note("notes/note3.md")
    {}
    """
    note_name = note_path.split("/")[-1].rsplit(".", 1)[0]
    file_path = note_path.rsplit('/',1)[0] + '/'
    if graph is None:
        graph = {}
    if note_name in graph:
        return graph

    with open(note_path, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = re.compile(r"\[\[(.*?)\]\]")
    names = pattern.findall(content)

    if names:
        graph.setdefault(note_name, [])
        for link in sorted(names):
            if link not in graph[note_name]:
                graph[note_name].append(link)
            build_graph_from_note(file_path + link + ".md", graph)

    return graph



def convert_to_dot(graph: dict):
    """
    >>> convert_to_dot({"note1": ["note2"], "note2": ["note1"]})
    >>> with open("graph.dot", "r") as f:
    ...     print(f.read())
    digraph {
    note1 -> note2
    note2 -> note1
    }
    """
    dot = "digraph {\n"
    for node in sorted(graph.keys()):
        for neighbor in sorted(graph[node]):
            dot += (f"{node} -> {neighbor}\n")
    dot += "}"

    with open("graph.dot", 'w', encoding='utf-8') as file_out:
        file_out.write(dot)

if __name__ == '__main__':
    build_graph_from_note('notes/note2.md')
    import doctest
    print(doctest.testmod())
